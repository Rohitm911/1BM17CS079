f1=open("prime.txt","r")
f2=open("happynumber.txt","r")
s1=f1.read()
s2=f2.read()
f1=read()
def check():
    count=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]== s2[j]:
                count=count+1
print(check())
