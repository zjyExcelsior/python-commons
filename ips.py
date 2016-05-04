# coding: utf-8
'''
some method about ip
'''
import socket
import urlparse


def get_ip_ranges(begin_ip, end_ip=''):
    '''
    '192.168.1.22', '192.168.3.33' -> '192.168.1-3.22-33'
    '''
    if not end_ip:
        return begin_ip
    begin_ip_list = begin_ip.split('.')
    end_ip_list = end_ip.split('.')
    result_ip_list = [''.join([begin, '-', end]) if begin !=
                      end else begin for begin, end in zip(begin_ip_list, end_ip_list)]
    return '.'.join(result_ip_list)


def get_sorted_ip_list(ip_list):
    '''
    对ip列表进行排序
    '''
    return sorted(ip_list, key=socket.inet_aton)

def is_valid_url(url):
    parts = urlparse.urlparse(url)
    return parts.scheme in ('http', 'https')

if __name__ == '__main__':
    print get_ip_ranges('192.168.1.22')  # 192.168.1.22
    print get_ip_ranges('192.168.1.22', '192.168.3.33')  # 192.168.1-3.22-33
    ip_list = ['192.168.1.33', '10.5.1.3', '10.5.2.4', '202.98.96.68', '133.120.1.1']
    print get_sorted_ip_list(ip_list)
    print is_valid_url('http://www.google.com')
    print is_valid_url('www.google.com')
