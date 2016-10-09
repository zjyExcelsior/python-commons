# coding: utf-8
"""
Some method about secret key
"""
import os
from base64 import b64encode

def get_key_urandom(length):
    """get secreat key by os.urandom()"""
    random_bytes = os.urandom(length)
    # random_bytes = open('/dev/urandom', 'rb').read(32)
    token = b64encode(random_bytes)
    # token = random_bytes.encode('base64') # 会多一个换行符
    # token = random_bytes.encode('hex')
    token = token[:length]
    return token

if __name__ == '__main__':
    print get_key_urandom(32)