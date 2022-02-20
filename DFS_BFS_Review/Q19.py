'''from itertools import product
n=4
a=list(product(['+','-','*','/'],repeat=(n-1)))
for i in a:
    x,y,z=i
    print(x,y,z)'''
n=6
a=[1,2,3,4,5,6]
# + - * //
add,sub,mul,div=2,1,1,1
maxx=-1e9
minn=1e9
def dfs(i,now):
    global add,sub,mul,div,maxx,minn
    if i==n:
        maxx=max(maxx,now)
        minn=min(minn,now)
        return
    else:
        if add>0:
            add-=1
            dfs(i+1,now+a[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-a[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*a[i])
            mul+=1
        if div>0:
            div-=1
            if now<0:
                dfs(i+1,abs(now)//a[i])
            else:
                dfs(i+1,now//a[i])
            div+=1
dfs(1,a[0])
print(maxx)
print(minn)