n,m,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort(reverse=True)
result=0

for i in range(1,m+1):
    if i%(k+1)==0:
        result+=array[1]
    else:
        result+=array[0]

print(result)