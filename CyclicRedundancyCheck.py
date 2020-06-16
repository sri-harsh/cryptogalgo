# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:52:33 2019

@author: Sriharsha
"""

ind=input("Enter the data to be sent= ")
#print(ind)
indiv=input("Enter the divisor= ")
le=len(indiv)
indu=ind
ind=ind+(le-1)*"0"
#print(ind)
elo=ind[:len(indiv)]
ind=ind[le:]
el=len(ind)
def xor(a,b):
    r=""
    for i in range(len(a)):
        x=""
        x=a[i]+b[i]
#        print(x)
        if x=="00" or x=="11":
            r=r+"0"
        elif x=="01" or x=="10":
            r=r+"1"
    return r
while el>=1:
    if elo[0]=="1":
        elo=xor(elo,indiv)
    else:
        elo=xor(elo,"0"*le)
    elo=elo[1:]
#    print(ind,"ind")
    elo=elo+ind[0]
    if len(ind)>1:
        ind=ind[1:]
    else:
        if elo[0]=="1":
            elo=xor(elo,indiv)
        else:
            elo=xor(elo,"0"*le)
        elo=elo[1:]
#        print(elo)
#        print("Done.")
        break
#    print(elo)
    el=el-1
indu=indu+elo
print("Remainder is=",elo)
print("Data to be sent is=",indu)
ind=input("Enter the data received= ")
print(ind)
elo=ind[:len(indiv)]
ind=ind[le:]
el=len(ind)
while el>=1:
    if elo[0]=="1":
        elo=xor(elo,indiv)
    else:
        elo=xor(elo,"0"*le)
    elo=elo[1:]
#    print(ind,"ind")
    elo=elo+ind[0]
    if len(ind)>1:
        ind=ind[1:]
    else:
        if elo[0]=="1":
            elo=xor(elo,indiv)
        else:
            elo=xor(elo,"0"*le)
        elo=elo[1:]
        print(elo)
        if "1" in elo:
            print("Error in data!")
        else:
            print("Data received without an error!")
#        print("Done.")
        break
#    print(elo)
    el=el-1
