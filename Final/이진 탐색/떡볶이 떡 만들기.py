n,m=map(int,input().split())
arr=list(map(int,input().split()))
def solution(n,m,arr):
    left=0
    right=max(arr)
    answer=0
    while left<=right:
        mid=(left+right)//2
        length=0
        for i in arr:
            if i-mid<0:
                continue
            length+=i-mid
        if length==m:
            answer=mid
            break
        if length>m:
            left=mid+1
            answer=mid
        elif length<m:
            right=mid-1
    return answer
print(solution(n,m,arr))
