n=int(input())
arr=[]
for _ in range(n):
    name,grade=map(str,input().split())
    arr.append((name,grade))
arr.sort(key=lambda x:x[1])
for i in arr:
    print(i[0],end=" ")