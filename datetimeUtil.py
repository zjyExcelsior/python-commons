# coding: utf-8
'''
一些关于时间的方法
'''
import datetime
import time

def datetime_to_timestamp(datetime_str):
    '''
    时间字符串 -> 时间戳
    '2016-04-21 18:06:20' -> 1461233180
    '''
    tmp_struct_time = time.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    timestamp = int(time.mktime(tmp_struct_time))
    return timestamp

def timestamp_to_datetime(timestamp):
    '''
    时间戳 -> 时间字符串
    1461233180 -> '2016-04-21 18:06:20'
    '''
    tmp_struct_time = time.localtime(timestamp)
    datetime_str = time.strftime('%Y-%m-%d %H:%M:%S', tmp_struct_time)
    return datetime_str

def previous_datetime(datetime_str, days=0):
    '''
    给定一个datetime字符串，返回该时间前days天的datetime字符串
    days=1 => '2016-04-21 18:06:20' -> '2016-04-20 18:06:20'
    '''
    dt = datetime.datetime
    return (dt.strptime(datetime_str, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')

def get_year():
    '''
    返回当前所处的年份
    '''
    dt = datetime.datetime
    return dt.today().strftime('%Y')

if __name__ == '__main__':
    timestamp = datetime_to_timestamp('2016-04-21 18:06:20')
    print timestamp
    print timestamp_to_datetime(timestamp)
    print previous_datetime('2016-04-21 18:06:20', 1)
    print get_year()