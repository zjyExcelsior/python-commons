# coding: utf-8
'''
some methods about regex
'''
import re

def find_word():
    '''
    获取 '2.11-0.9.0.1'(re.findall())
    '''
    sentence = 'my_dev/kafka_2.11-0.9.0.1/bin/'
    reg_expr = r'kafka_(.*?)/' # ?是为了不贪婪匹配
    return re.findall(reg_expr, sentence)

def make_valid_nickname(nickname):
    '''
    去除不符合规则的字符(re.sub())
    '''
    return re.sub(r'[^a-zA-Z0-9_.]', '', nickname)

if __name__ == '__main__':
    # print find_word()
    print make_valid_nickname('<p>zhujiongyao</p>...')