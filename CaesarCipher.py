inp="PHHW PH DIWHU WKH WRJD SDUWB"
hey="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ki=0
for key in range(0,26):
    haha=""
    for i in range(len(inp)):
        if inp[i]!=" ":
            ki=hey.index(inp[i])
        #    print(ki)
            if ki+key<=len(hey)-1:
        #        print("here")
                haha=haha+hey[ki+key]
            else:
                ki=ki-26
                haha=haha+hey[ki+key]
        elif inp[i]==" ":
            haha=haha+" "
    print(haha)
    print(key)
file=open("output2.txt","w")
file.write("output is "+haha)
file.close()
#another method
"""
ccount=0
wcount=0
file=open("haha.txt","r")
filey=open("output1.txt","w")
for i in file.read():
    if i!=" ":
        ccount+=1
print(ccount)
filey.write("Character count is "+str(ccount)+"\n")
file.close()
wcount=0
file=open("haha.txt","r")
for j in file.readlines():
    j=j.split()
    wcount+=len(j)
print(wcount)
filey.write("Word count "+str(wcount)+"\n")
file.close()
file=open("haha.txt","r")
for j in file.read():
    if j!=" ":
        print("ascii val",ord(j))
        filey.write("ascii val "+str(ord(j))+"\n")
file.close()
filey.close()
"""
