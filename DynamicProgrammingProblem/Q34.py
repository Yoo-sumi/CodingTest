n=7
array=[15,11,4,8,5,2,4]
array.reverse()
dp=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[i]>array[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)
print(n-max(dp))
#[1, 2, 3, 3, 4, 5, 5]