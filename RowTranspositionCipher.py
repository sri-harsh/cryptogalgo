# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 11:14:51 2019

@author: Sriharsha
"""
import random
text=input("Enter the string= ")
l=len(text)
kes=int(input("Enter the size of the key= "))
ket=""
if l%kes==0:
    for i in range(kes):
        ket=ket+random.randint(1,len(kes))
else:
    a="abcdefghijklmnopqrstuvwxyz"
    lo=len(a)-(l%kes)
    text=text+a[lo+1:]
#    print(len(text))
#    print(text)
    emp=[]
    for i in range(kes):
        flag=0
        while flag==0:
            l=random.randint(1,kes)
            if l not in emp:
                emp.append(l)
                ket=ket+str(l)
                flag=1
#print(ket)
#print(kes)
#ket="4312567"
#print(ket)
def encryrowt(text,kes,ket):
    k=0
    flag=0
    encryp=[]
    ro=len(text)/kes
    ro=int(ro)
    for i in range(ro):
        encryp.append([])
    for i in range(len(text)):
        encryp[flag].append(text[i])
        k=k+1
        if k==kes:
            k=0
            flag=flag+1
#            print(flag)
#    print(encryp)
    entext={}
    for i in ket:
        entext[str(i)]=""
#    print(entext)
    k=0
    for i in ket:
#        print(i)
        for j in encryp:
            entext[i]+=j[k]
        k=k+1
#    k=0
#    flag=0
#    for i in ket:
#        for j in encryp:
#            k=k+1
#            entext[flag].append(j[int(i)-1])
#            if k==ro:
#                flag=flag+1
#                k=0
#    print(entext)
    encrt=""
    for i in range(1,kes+1):
#        print(i)
        encrt+=entext[str(i)]
    print("Encrypted text=",encrt)
    return encrt
en=encryrowt(text,kes,ket)
#en=encryrowt(en,kes,ket)
def decry(text,kes,ket):
    dec=[]
    o=len(text)/kes
    o=int(o)
    for i in range(kes):
        dec.append([])
#    print(dec)
    k=0
    flag=0
    for i in range(len(text)):
        dec[flag].append(text[i])
        k=k+1
        if k==o:
            k=0
            flag=flag+1
#    print(dec)
    decdi={}
    for i in ket:
        decdi[i]=""
    for i in range(1,kes+1):
        decdi[str(i)]=dec[i-1]
#    print(decdi)
    decy={}
    dectext=""
    for j in range(o):
        decy[str(j)]=""
    flag=0
    k=0
    for i in decdi.values():
        for j in range(len(i)):
            decy[str(j)]+=i[j]
#    print(decy)
    for i in decy.values():
        dectext+=i
    print("Decrypted text=",dectext)
    return dectext

de=decry(en,kes,ket)
#de=decry(de,kes,ket)
