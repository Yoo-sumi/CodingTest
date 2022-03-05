n,m=map(int,input().split())
edges=[]
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
result=[]
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
    cost,a,b=edge
    if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        result.append(cost)
print(sum(result)-max(result))