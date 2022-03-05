n,m=7,11
edges=[]
parent=[0]*(n+1)
sum=0
for i in range(1,n+1):
    parent[i]=i
for i in range(m):
    x,y,cost=map(int,input().split())
    edges.append((cost,x,y))
    sum+=cost
edges.sort()
result=0
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
for edge in edges:
    cost,x,y=edge
    if find_parent(x)!=find_parent(y):
        union_parent(x,y)
        result+=cost
print(sum-result)