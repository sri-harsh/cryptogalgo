# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:24:35 2019

@author: Sriharsha
"""
s=[]
k=[10,100,11,200] #if you want take string
keylen=len(k)
T=[]
for i in range(256):
    s.append(i)
    T.append(k[i%keylen])
j=0

for i in range(256):
    j=(j+s[i]+T[i])%256
#    print(len(s))
#    print(i,j)
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
el=input("Enter the message= ")
#for i in range(len(el)):
#    print(ord(el[i]))    


def bina(a):
    bi=""
    while a>0:
        bi=bi+str(a%2)
        a=a//2
    return bi[::-1]
#print(bina(97))
ellu=[]
#for i in el:
#    print(ord(i))
for i in el:
    ellu.append(bina(ord(i)))

fla=0
i=0
j=0
asalkey=[]
while True:
    i=(i+1)%256
    j=(j+s[i])%256
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    t=(s[i]+s[j])%256
    k1=s[t]
    asalkey.append(k1)
    fla=fla+1
    if fla==len(ellu):
        break
#print(k1)
#print(asalkey)
fkey=[]
for i in asalkey:
    fkey.append(bina(i))
print("asal",asalkey)
for i in range(len(fkey)):
    if len(fkey[i])<len(ellu[i]):
        fkey[i]='0'*(len(ellu[i])-len(fkey[i]))+fkey[i]
    elif len(fkey[i])>len(ellu[i]):
        ellu[i]='0'*(len(fkey[i])-len(ellu[i]))+ellu[i]
#print(ellu)
print("Encrypting the message with below key: ")
print(fkey)
def xor1(a,b):
    l=len(a)
    res=""
    for i in range(l):
        if a[i]=='0' and b[i]=='0':
            res=res+"0"
        elif a[i]=='1' and b[i]=='0':
            res=res+"1"
        elif a[i]=='0' and b[i]=='1':
            res=res+"1"
        elif a[i]=='1' and b[i]=='1':
            res=res+"0"
    return res
ent=[]
for i in range(len(ellu)):
    ent.append(xor1(ellu[i],fkey[i]))
#print("Encrypted message is ",ent)
def decim(a):
    flag=0
    l=len(a)
    dec=0
    a=a[::-1]
    for i in range(l):
        if a[i]=="1":
            dec=dec+2**flag
        flag=flag+1
#    print(dec)
    return dec
enctxt=""
for i in ent:
#    print(decim(i))
#    print(chr(decim(i)))
    enctxt=enctxt+chr(decim(i))
print("Encrypted text is= ",enctxt)
fid=[]
#print(ent)
for i in ent:
    fid.append(decim(i))
#print("conv",fid)

tobina=[]
for i in fid:
    tobina.append(bina(i))
#print(tobina)
for i in range(len(fkey)):
    if len(fkey[i])<len(tobina[i]):
        fkey[i]='0'*(len(tobina[i])-len(fkey[i]))+fkey[i]
        
    elif len(fkey[i])>len(tobina[i]):
        tobina[i]='0'*(len(fkey[i])-len(tobina[i]))+tobina[i]
    
xorru=[]
#print(tobina)
#print(fkey)
for i in range(len(ellu)):
    xorru.append(xor1(tobina[i],fkey[i]))
#print("final",xorru)
al=""
for i in xorru:
#    print(chr(decim(i)))
    al=al+chr(decim(i))
print("Decrypted text= ",al)
