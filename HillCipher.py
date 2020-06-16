# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:40:06 2019

@author: Sriharsha
"""

txt=input("Enter the keyword= ")
txt=txt.lower()
print(txt)
keymat=[]
n=len(txt)
if n==4:
    n=2
elif n==9:
    n=3
for i in range(n):
    keymat.append([])
l=0
k=0
for i in txt:
    keymat[k].append(i)
    if l==n-1:
        l=0
        k=k+1
    else:
        l=l+1
for i in range(len(keymat)):
    for j in range(len(keymat[i])):
        keymat[i][j]=ord(keymat[i][j])-97
print(keymat)
deta=0
if n==2:
    deta=keymat[0][0]*keymat[1][1]-keymat[0][1]*keymat[1][0]
if n==3:
    deta=keymat[0][0]*(keymat[1][1]*keymat[2][2]-keymat[1][2]*keymat[2][1])-keymat[0][1]*(keymat[1][0]*keymat[2][2]-keymat[1][2]*keymat[2][0])+keymat[0][2]*(keymat[1][0]*keymat[2][1]-keymat[1][1]*keymat[2][0])
while deta<0:
   deta=deta+26
print(deta)
def gcd(a,b):  
    if (b==0): 
         return a 
    return gcd(b,a%b)
if gcd(deta,26)==1:
    pt=input("Enter the text you want to encrypt= ")
    pt=pt.lower()
    pt1=""
    for i in pt:
        if i!=" ":
            pt1=pt1+i
    pt=pt1
    my_list=[]
    for i in pt:
        my_list.append(i)
    final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]  
    for i in final:
        if (len(i)==1 and n==2):
            i.append("x")
        elif len(i)==2 and n==3:
            i.append("x")
        elif len(i)==1 and n==3:
            i.append("x")
            i.append("x")
    print(final)
    for i in range(len(final)):
        for j in range(len(final[i])):
            final[i][j]=ord(final[i][j])-97
    print(final)
    def matmul(m1,m2):
        resu=[]
        for i in range(len(m1)):
            resu.append([])
            for j in range(len(m2[0])):
                resu[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    resu[i][j]+= m1[i][k]*m2[k][j]
        return resu
    el=[]
    result=[]
    for i in final:
        for j in i:
            el.append([j])
        ki=matmul(keymat,el)
        result.append(ki)
        el=[]
    res=""
    for i in result:
        for j in i:
            for kee in j:
                res+=str(kee)+" "
    res=res.split()
    finnu=[]
    for i in res:
        i=int(i)
        i=i%26
        i=i+97
        i=chr(i)
        finnu.append(i)
    finnu="".join(finnu)
    print(finnu.upper())
    inp1=input("Enter the text to decrypt= ")
    inp1=inp1.lower()
    pt1=""
    for i in inp1:
        if i!=" ":
            pt1=pt1+i
    inp1=pt1
    my_list=[]
    for i in inp1:
        my_list.append(i)
    final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]  
    for i in final:
        if len(i)==1 and n==2:
            i.append("x")
        elif len(i)==2 and n==3:
            i.append("x")
        elif len(i)==1 and n==3:
            i.append("x")
            i.append("x")
    print(final)
    for i in range(len(final)):
        for j in range(len(final[i])):
            final[i][j]=ord(final[i][j])-97
    count=1
    det=deta
    while 1:
        if deta%26==1:
            break
        deta=deta+det
        count+=1
    print(count)
    if n==2:
        decm=[[keymat[1][1],-keymat[0][1]],[-keymat[1][0],keymat[0][0]]]
        for i in range(2):
            for j in range(2):
                while decm[i][j]<0:
                    decm[i][j]+=26
        for i in range(2):
            for j in range(2):
                decm[i][j]=count*decm[i][j]
        print(decm)
    elif n==3:
        decl=[]
        for hey in range(3):
            decl.append([])
        for il in decl:
            il.append([])
            il.append([])
            il.append([])
        decm=[[keymat[1][1]*keymat[2][2]-keymat[1][2]*keymat[2][1],-(keymat[1][0]*keymat[2][2]-keymat[1][2]*keymat[2][0]),keymat[1][0]*keymat[2][1]-keymat[1][1]*keymat[2][0]],[-(keymat[0][1]*keymat[2][2]-keymat[2][1]*keymat[0][2]),keymat[0][0]*keymat[2][2]-keymat[0][2]*keymat[2][0],-(keymat[0][0]*keymat[2][1]-keymat[0][1]*keymat[2][0])],[keymat[0][1]*keymat[1][2]-keymat[1][1]*keymat[0][2],-(keymat[0][0]*keymat[1][2]-keymat[0][2]*keymat[1][0]),keymat[0][0]*keymat[1][1]-keymat[1][0]*keymat[0][1]]]
        for i in range(3):
            for j in range(3):
                if i!=j:
                    decl[i][j]=count*decm[j][i]
                elif i==j:
                    decl[i][j]=count*decm[i][j]
        for i in range(3):
            for j in range(3):
                while decl[i][j]<0:
                    decl[i][j]+=26
        decm=decl
        print(decm)
    el=[]
    result=[]
    for i in final:
        for j in i:
            el.append([j])
        ki=matmul(decm,el)
        result.append(ki)
        el=[]
    res=""
    for i in result:
        for j in i:
            for kee in j:
                res+=str(kee)+" "
    res=res.split()
    finnu=[]
    for i in res:
        i=int(i)
        i=i%26
        i=i+97
        i=chr(i)
        finnu.append(i)
    finnu="".join(finnu)
    print(finnu.upper())
else:
    print("Not possible!")