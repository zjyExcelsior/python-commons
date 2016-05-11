# coding: utf-8
def switch(item):
    '''a replacement method for switch statement in Python'''
    return {
        'one': 1,
        'two': 2,
        'three': 3
    }.get(item, 0)

if __name__ == '__main__':
    print switch('one')
    print switch('two')
    print switch('three')
    print switch('default')
