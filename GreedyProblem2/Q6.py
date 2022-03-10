import heapq
food_times=[1,0,0]
k=1
def solution(food_times,k):
    if sum(food_times)<=k:
        return -1
    n=len(food_times)
    q=[]
    for i in range(n):
        heapq.heappush(q,(food_times[i],i+1))
    print(q)
    while True:
        now=heapq.heappop(q)
        if k-now[0]*n<0:
            heapq.heappush(q,now)
            break
        k-=now[0]*n
        n-=1

    q.sort(key=lambda x:x[1])
    result=q[k%n][1]
    return result

print(solution(food_times,k))