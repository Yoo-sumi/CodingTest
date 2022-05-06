n,k=map(int,input().split())

def dfs(num,count):
    if num==1:
        return count
    if num<1:
        return 1e9
    a=dfs(num-1,count+1)
    b=1e9
    if num%k==0:
        b=dfs(num//k,count+1)
    return min(a,b)
print(dfs(n,0))