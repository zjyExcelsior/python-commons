# coding: utf-8
'''
some method about ip
'''


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

if __name__ == '__main__':
    print get_ip_ranges('192.168.1.22') # 192.168.1.22
    print get_ip_ranges('192.168.1.22', '192.168.3.33') # 192.168.1-3.22-33