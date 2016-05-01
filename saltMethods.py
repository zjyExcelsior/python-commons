# coding: utf-8
'''
some methods about salt
'''
# need super privileges
import salt.config
import salt.key
import salt.client
import salt.wheel
from salt.exceptions import SaltClientError
from logger import get_logger

salt_logger = get_logger('salt')


def get_minion_status(salt_client, master_opts):
    '''
    Print the status of all known salt minions
    '''
    ret = {}
    try:
        minions = salt_client.cmd('*', 'test.ping', timeout=master_opts.get('timeout'))
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
            delete_key(minion)
    return ret

def delete_key(minion_id):
    # wheel = salt.wheel.Wheel(master_opts)
    # wheel.call_func('key.delete', match=minion)
    wheel = salt.wheel.WheelClient(master_opts)
    wheel.cmd('key.delete', [minion_id])

def get_all_keys(master_opts):
    key = salt.key.Key(master_opts)
    keys = key.list_keys()
    return keys.get('minions', [])


if __name__ == '__main__':
    salt_client = salt.client.LocalClient()
    master_opts = salt.config.client_config('/etc/salt/master')
    # print get_minion_status(salt_client, master_opts)
    # print get_minion_up(salt_client, master_opts)
    # print get_minion_down(salt_client, master_opts)
    # print get_minion_down(salt_client, master_opts, removekeys=True)
    # print get_minion_status(salt_client, master_opts)
    # print get_all_keys(master_opts)
    print get_minion_status(salt_client, master_opts)
