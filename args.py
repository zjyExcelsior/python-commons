# coding: utf-8
'''
argparse examples
'''
import argparse


def _get_args():
    '''
    get args from command line:
    $ python args.py --name zhujiongyao
    -> _get_args().name == 'zhujiongyao'
    '''
    parser = argparse.ArgumentParser(description='arguments for args.py')
    parser.add_argument(
        '--name', type=str, required=True, default='', help='name')
    return parser.parse_args()


def get_name(name):
    return name

if __name__ == '__main__':
    args = _get_args()
    print get_name(args.name)
