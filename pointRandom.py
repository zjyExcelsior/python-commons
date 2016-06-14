# coding: utf-8
'''
得到根据网格划分的随机点的坐标
'''
from random import uniform as uniform_random

# 画布总宽度
WIDTH = 1440
HEIGHT = 900

# 每个方块的大小
WIDTH_EACH = 144
HEIGHT_EACH = 90

# 每行／列的方块个数
X_NUM = WIDTH / WIDTH_EACH
Y_NUM = HEIGHT / HEIGHT_EACH


def get_point(index):
    quotient, remainder = divmod(index, X_NUM)
    x = WIDTH_EACH * remainder + uniform_random(0, WIDTH_EACH - 30)
    y = HEIGHT_EACH * quotient + uniform_random(0, HEIGHT_EACH - 30)
    return (x, y)

if __name__ == '__main__':
    for i in xrange(10):
        print get_point(i)
