def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n, m=map(int,input().split())

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

edges=[]
for i in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()
result=0
last=0
for i in range(m):
    cost,a,b=edges[i]
    if find_parent(parent,a)!=find_parent(parent,b):
        union(parent,a,b)
        result+=cost
        last=cost
print(result-last)
