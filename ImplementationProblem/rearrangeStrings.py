s=str(input())
a=[]
n=[]
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        n.append(int(i))
    else: #i.isalpha()
        a.append(i)
a.sort()
if len(n)>0:
    a.append(str(sum(n)))
for i in a:
    print(i,end="")

