n=int(input())
store=[-1]*(n+1)
def dfs(num,count):
    a=[]
    if num==1:
        return count
    if num<1:
        return 1e9
    if num%5==0:
        a.append(dfs(num//5,count+1))
    if num%3==0:
        a.append(dfs(num//3,count+1))
    if num%2==0:
        a.append(dfs(num//2,count+1))
    a.append(dfs(num-1,count+1))
    return min(a)
print(dfs(n,0))
