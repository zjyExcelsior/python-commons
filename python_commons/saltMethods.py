# coding: utf-8
"""
some methods about salt
"""
# need super privileges
import salt.config
import salt.key
import salt.client
import salt.wheel
import salt.runner
from salt.exceptions import SaltClientError
from logger import get_logger

salt_logger = get_logger('salt')


def get_minion_status(salt_client, master_opts):
    """
    Print the status of all known salt minions
    """
    ret = {}
    try:
        minions = salt_client.cmd(
            '*', 'test.ping', timeout=master_opts.get('timeout'))
    except SaltClientError as client_error:
        salt_logger.exception(
            'salt-master is down, Traceback info:\n %s', client_error)
        return ret
    keys = get_all_keys(master_opts)
    # keys == {'minions_rejected': [], 'minions_denied': [], 'minions_pre': [], 'minions': []}
    # ret['all_minions'] = sorted(keys.get(minions))
    ret['up'] = sorted(minions)
    ret['down'] = sorted(set(keys) - set(minions))
    return ret


def get_minion_up(salt_client, master_opts):
    ret = get_minion_status(salt_client, master_opts).get('up', [])
    return ret


def get_minion_down(salt_client, master_opts, removekeys=False):
    ret = get_minion_status(salt_client, master_opts).get('down', [])
    for minion in ret:
        if removekeys:
            _delete_key(minion)
    return ret

def get_minion_alived(salt_runner):
    """返回alived状态的minions"""
    minions_alived = salt_runner.cmd('manage.alived')
    if not minions_alived:
        salt_logger.exception('there is no alived minions')
    return minions_alived


def _delete_key(minion_id):
    # wheel = salt.wheel.Wheel(master_opts)
    # wheel.call_func('key.delete', match=minion)
    wheel = salt.wheel.WheelClient(master_opts)
    wheel.cmd('key.delete', [minion_id])


def get_all_keys(master_opts):
    key = salt.key.Key(master_opts)
    keys = key.list_keys()
    return keys.get('minions', [])


def sync_modules(salt_client):
    salt_client.cmd(minion_ids, 'saltutil.sync_modules', expr_form='list')


if __name__ == '__main__':
    salt_client = salt.client.LocalClient()
    master_opts = salt.config.client_config('/etc/salt/master')
    # salt_runner = salt.runner.Runner(master_opts)
    # print get_minion_alived(salt_runner)
    # print get_minion_status(salt_client, master_opts)
    # print get_minion_up(salt_client, master_opts)
    # print get_minion_down(salt_client, master_opts)
    # print get_minion_down(salt_client, master_opts, removekeys=True)
    # print get_minion_status(salt_client, master_opts)
    # print get_all_keys(master_opts)
    print get_minion_status(salt_client, master_opts)
