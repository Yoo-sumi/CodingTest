n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
result=1
while True:
    value=result
    for i in range(n):
        if value>=data[i]:
            value-=data[i]
            if value==0:
                result+=1
    if value>0:
        break
print(result)

