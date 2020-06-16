# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:35:13 2019

@author: Sriharsha
"""

hey="abcdefghijklmnopqrstuvwxyz"
key="andrewicksohtbfgjlmpquvxyz"
msg="seemseaomedsamhl"
res=""
for i in msg:
    k=hey.index(i)
    h=key[k]
#    print(h)
    res=res+h
print(res)
