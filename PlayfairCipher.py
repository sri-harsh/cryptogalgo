# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:38:43 2019

@author: Sriharsha
"""

txt=input("Enter the keyword= ")
keymat=[]
for i in range(5):
    keymat.append([])
k=0
l=0
hey="abcdefghijklmnopqrstuvwxyz"
tra=[]
for i in txt:
    if (i=="i" or i=="j") and (i not in tra):
#        print(i)
        keymat[l].append("i/j")
        tra.append("i")
        tra.append("j")
        k=k+1
    elif i not in tra:
#        print(i)
        keymat[l].append(i)
        tra.append(i)
        k=k+1
#    print(k)
    if k==5:
        l=l+1
        k=0
#print(l,k)
for i in hey:
    if i not in tra and i!="i" and i!="j":
#        print(l)
        keymat[l].append(i)
        tra.append(i)
        k=k+1
    if (i=="j" or i=="i") and (i not in tra):
        keymat[l].append("i/j")
        tra.append("i")
        tra.append("j")
        k=k+1
    if k==5:
        l=l+1
        k=0
    if l==5:
        break
print(keymat)


haha=input("Enter the message to encrypt= ")
my_list=[]
for i in haha:
    my_list.append(i)
p=0
pl=[]
rs=""
n=2
for i in range(len(my_list)-1):
    if i%2==0 and my_list[i+1]==my_list[i]:
        my_list.insert(i+1,"x")
print(my_list)
final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]
#print(final)
finallo=[]
for i in range(len(final)):
    if len(final[i])==2:
        if final[i][0]==final[i][1]:
    #        print("going")
            finallo.append([final[i][0],"x"])
#            finallo.append([final[i][0],"x"])
        else:
            finallo.append(final[i])
    else:
        finallo.append([final[i][0],"x"])
print(finallo)

encry=[]
enrytext=""
for i in finallo:
    for j in range(5):
        if i[0]=="i" or i[0]=="j":
            i[0]="i/j"
        if i[1]=="i" or i[1]=="j":
            i[1]="i/j"
        if (i[0] in keymat[j]):
            (k1,k2)=(j,keymat[j].index(i[0]))
#            print(k1,k2)
        if (i[1] in keymat[j]):
            (k3,k4)=(j,keymat[j].index(i[1]))
#            print(k3,k4)
    if k1==k3:
        if k2<=3 and k4<=3:
            enct=keymat[k1][k2+1]
            enct1=keymat[k1][k4+1]
        elif k2==4 and k4==4:
            enct=keymat[k1][0]
            enct1=keymat[k1][0]
        elif k2==4 and k4<=3:
            enct=keymat[k1][0]
            enct1=keymat[k1][k4+1]
        elif k2<=3 and k4==4:
            enct=keymat[k1][k2+1]
            enct1=keymat[k1][0]
#print(enrytext)
    elif k2==k4:
        if k1<=3 and k3<=3:
            enct=keymat[k1+1][k2]
            enct1=keymat[k3+1][k2]
        elif k1==4 and k3==4:
            enct=keymat[0][k2]
            enct1=keymat[0][k2]
        elif k1==4 and k3<=3:
            enct=keymat[0][k2]
            enct1=keymat[k3+1][k2]
        elif k1<=3 and k3==4:
            enct=keymat[k1+1][k2]
            enct1=keymat[0][k2]
    else:
        enct=keymat[k1][k4]
        enct1=keymat[k3][k2]
    enct=enct[:1]
    enct1=enct1[:1]
#    print(enct,enct1)
    enc=enct+enct1
    enrytext+=enc



print(enrytext)





haha=input("Enter the message to decrypt= ")
my_list=[]
for i in haha:
    my_list.append(i)
p=0
pl=[]
rs=""
n=2
final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]
#print(final)
finallo=[]
for i in range(len(final)):
    if len(final[i])==2:
        if final[i][0]==final[i][1]:
    #        print("going")
            finallo.append([final[i][0],"x"])
            finallo.append([final[i][0],"x"])
        else:
            finallo.append(final[i])
    else:
        finallo.append([final[i][0],"x"])
#print(finallo)

decry=[]
derytext=""
#print(final)
#print(finallo)
for i in finallo:
    for j in range(5):
        if i[0]=="i" or i[0]=="j":
            i[0]="i/j"
        if i[1]=="i" or i[1]=="j":
            i[1]="i/j"
        if (i[0] in keymat[j]):
            (k1,k2)=(j,keymat[j].index(i[0]))
#            print(k1,k2)
        if (i[1] in keymat[j]):
            (k3,k4)=(j,keymat[j].index(i[1]))
#            print(k3,k4)
#    print(k1,k2)
#    print(k3,k4)
    if k1==k3:
        if k2>=1 and k4>=1:
            enct=keymat[k1][k2-1]
            enct1=keymat[k1][k4-1]
        elif k2==0 and k4==0:
            enct=keymat[k1][4]
            enct1=keymat[k1][4]
        elif k2==0 and k4>=1:
            enct=keymat[k1][4]
            enct1=keymat[k1][k4-1]
        elif k2>=1 and k4==0:
            enct=keymat[k1][k2-1]
            enct1=keymat[k1][4]
#print(enrytext)
    elif k2==k4:
        if k1>=1 and k3>=1:
            enct=keymat[k1-1][k2]
            enct1=keymat[k3-1][k2]
        elif k1==0 and k3==0:
            enct=keymat[4][k2]
            enct1=keymat[4][k2]
        elif k1==0 and k3>=1:
            enct=keymat[4][k2]
            enct1=keymat[k3-1][k2]
        elif k1>=1 and k3==0:
            enct=keymat[k1-1][k2]
            enct1=keymat[4][k2]
    else:
#        print("going")
        enct=keymat[k1][k4]
        enct1=keymat[k3][k2]
    enct=enct[:1]
    enct1=enct1[:1]
#    print(enct,enct1)
    ok=enct+enct1
    derytext+=ok



print(derytext)
