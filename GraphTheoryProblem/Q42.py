G=4
P=3

parent=[0]*(G+1)
for i in range(1,G+1):
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
result=0
flag=False
for _ in range(P):
    a=int(input())
    if find_parent(a)==0:
        flag=True
        continue
    if flag==False:
        union_parent(find_parent(a),find_parent(a)-1)
        result+=1
    print(parent)
print(result)
print(parent)