n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n):
        if a[j]==1:
            union_parent(i+1,j+1)
city=list(map(int,input().split()))
result=[]
for i in city:
    result.append(parent[i+1])

if len(set(result))==1:
    print("YES")
else:
    print("NO")

