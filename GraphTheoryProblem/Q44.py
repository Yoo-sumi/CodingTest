n=5
array=[
    [],
    [11,-15,-15],
    [14,-5,-15],
    [-1,-1,-5],
    [10,-4,-1],
    [19,-4,19]
]
x=[]
y=[]
z=[]
for i in range(1,n+1):
    data=list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
x.sort()
y.sort()
z.sort()
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
edges=[]
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))
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
print(result)