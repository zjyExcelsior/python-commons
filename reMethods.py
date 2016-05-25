# coding: utf-8
'''
some methods about regex
'''
import re

def find_word():
    #获取 '2.11-0.9.0.1'
    sentence = 'my_dev/kafka_2.11-0.9.0.1/bin/'
    reg_expr = r'kafka_(.*?)/' # ?是为了不贪婪匹配
    return re.findall(reg_expr, sentence)

if __name__ == '__main__':
    print find_word()