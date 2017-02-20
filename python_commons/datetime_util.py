# coding: utf-8
"""
一些关于时间表达式转换的方法
"""

import datetime
from datetime import datetime as dt
import time


def datetime_to_timestamp(datetime_str, format='%Y-%m-%d %H:%M:%S'):
    """时间字符串(local) -> 时间戳
    '2016-04-21 18:06:20' -> 1461233180
    """
    struct_time = time.strptime(datetime_str, format)
    timestamp = int(time.mktime(struct_time))
    return timestamp


def timestamp_to_datetime(timestamp, format='%Y-%m-%d %H:%M:%S'):
    """时间戳 -> 时间字符串(local)
    1461233180 -> '2016-04-21 18:06:20'
    """
    datetime_obj = dt.fromtimestamp(timestamp)
    datetime_str = datetime_obj.strftime(format)
    return datetime_str


def previous_datetime(datetime_str, days=0, format='%Y-%m-%d %H:%M:%S'):
    """给定一个datetime字符串(local)，返回该时间前days天的datetime字符串
    days=1 => '2016-04-21 18:06:20' -> '2016-04-20 18:06:20'
    """
    return (dt.strptime(datetime_str, format)
            - datetime.timedelta(days=days)).strftime(format)


def get_year():
    """返回当前所处的年份"""
    return dt.today().strftime('%Y')

if __name__ == '__main__':
    timestamp = datetime_to_timestamp('2016-04-21 18:06:20')
    print timestamp
    print timestamp_to_datetime(timestamp)
    print previous_datetime('2016-04-21 18:06:20', 1)
    print get_year()
