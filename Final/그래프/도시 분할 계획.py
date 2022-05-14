n,m=map(int,input().split())
parent=[]
edges=[]
for i in range(n+1):
    parent.append(i)

def find_parent(parent,v):
    if parent[v]!=v:
        parent[v]=find_parent(parent,parent[v])
    return parent[v]
def union_parent(a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()
result=0
last=0
for c,a,b in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(a,b)
        result+=c
        last=c
print(result-last)
