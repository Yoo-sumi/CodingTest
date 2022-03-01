def edit_dist(str1,str2):
    n=len(str1)
    m=len(str2)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0]=i
    for i in range(1,m+1):
        dp[0][i]=i

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    print(dp)
    return dp[n][m]
print(edit_dist("saturday","sunday"))
#[[0, 1, 2, 3, 4, 5], [1, 1, 2, 3, 3, 4], [2, 2, 2, 3, 4, 4], [3, 2, 3, 3, 4, 5], [4, 3, 3, 4, 4, 5], [5, 4, 4, 3, 4, 5], [6, 5, 5, 4, 3, 4], [7, 6, 6, 5, 4, 3]]
