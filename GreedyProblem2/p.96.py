n,m=map(int,input().split())
array=[[] for _ in range(n)]
result=0
for _ in range(n):
    a=list(map(int,input().split()))
    result=max(result,min(a))

print(result)