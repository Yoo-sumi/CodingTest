n=int(input())
dp=[]

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            up_left=0
        else:
            up_left=dp[i-1][j-1]

        if j==i:
            up=0
        else:
            up=dp[i-1][j]

        dp[i][j]=dp[i][j]+max(up_left,up)
#[[7], [10, 15], [18, 16, 15], [20, 25, 20, 19], [24, 30, 27, 26, 24]]
print(max(dp[n-1]))
print(dp)