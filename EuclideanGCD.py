def gcd(m, b):
    if m == 0 :
        return b
    return gcd(b%m, m)
m=int(input("Enter m:"))
b=int(input("Enter b:"))
print("gcd(m,b) = ", gcd(m, b))
[a1,a2,a3]=[1,0,m]
[b1,b2,b3]=[0,1,b]
while(True):
    if b3==0:
        print("Gcd of m,b:",b3)
        break
    if b3==1:
        if b2<0:
            b2=b2+m
            print("Inverse",b2)
        else:
            print("Inverse",b2)
        break
    Q=int(a3/b3)
    t1=a1-Q*b1
    t2=a2-Q*b2
    t3=a3-Q*b3
    [a1,a2,a3]=[b1,b2,b3]
    [b1,b2,b3]=[t1,t2,t3]
