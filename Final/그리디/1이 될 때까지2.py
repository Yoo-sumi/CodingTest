n,k=map(int,input().split())
count=0
while n!=1:
    if n<k:
        break
    a=(n//k)*k
    count+=(n-a)
    n=a
    while True:
        if n%k!=0:
            break
        n//=k
        count+=1
if n>1:
    count+=(n-1)
print(count)
