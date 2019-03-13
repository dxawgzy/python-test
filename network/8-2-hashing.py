#coding=utf8
#!usr/bin/python
__author__ = 'igis_gzy'  # P128

import hashlib

def alpha_shard(word):
    if word[0] in 'abcdef':
        return 'server0'
    elif word[0] in 'ghijklm':
        return 'server1'
    elif word[0] in 'nopqrs':
        return 'server2'
    else:
        return 'server3'

def hash_shard(word):
    return 'server%d' % (hash(word) % 4)

def md5_shard(word):
    return 'server%d' % (ord(hashlib.md5(word).digest()[-1]) % 4)

words = open('E:/python/network2/words').read().split()

for function in alpha_shard, hash_shard, md5_shard:
    d = {'server0':0, 'server1':0, 'server2':0, 'server3':0}
    for word in words:
        d[function(word.lower())] += 1
    print function.__name__[:-6], d

"""
# function.__name__[:-6] 表示去掉函数名末尾6位字符（此处即去掉 _shard ）
alpha {'server0': 103, 'server1': 66, 'server2': 74, 'server3': 106}
hash {'server0': 71, 'server1': 98, 'server2': 103, 'server3': 77}
md5 {'server0': 91, 'server1': 97, 'server2': 71, 'server3': 90}

# function.__name__[:6] 取函数名的前6位字符
alpha_ {'server0': 103, 'server1': 66, 'server2': 74, 'server3': 106}
hash_s {'server0': 71, 'server1': 98, 'server2': 103, 'server3': 77}
md5_sh {'server0': 91, 'server1': 97, 'server2': 71, 'server3': 90}
"""

