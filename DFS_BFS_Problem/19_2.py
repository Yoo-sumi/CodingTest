n=3
a=[3,4,5]
# + - * //
ex=[1,0,1,0]
'''n=6
a=[1,2,3,4,5,6]
# + - * //
ex=[2,1,1,1]'''
s=["+","-","*","/"]
w=[]
def change(result,i,j):
    index=j+(i-1)
    if w[index]=="+":
        return result+a[i]
    elif w[index]=="-":
        return result-a[i]
    elif w[index]=="*":
        return result*a[i]
    elif w[index]=="/":
        if result<0:
            return -(abs(result)//a[i])
        return result//a[i]
def dfs(count,ss):
    global w
    if count==n-1:
        w+=ss
        return
    for i in range(len(ex)):
        if ex[i]!=0:
            ex[i]-=1
            dfs(count+1,ss+s[i])
            ex[i]+=1
dfs(0,"")
maxx=-1e9
minn=1e9
for j in range(0,len(w),n-1):
    result=a[0]
    for i in range(1,n):
        result=change(result,i,j)
    maxx=max(result,maxx)
    minn=min(result,minn)
print(maxx)
print(minn)





