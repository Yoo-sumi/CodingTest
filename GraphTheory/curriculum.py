from collections import deque
import copy
n=int(input())
point=[0]*(n+1)
time=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    for j in data[1:-1]:
        point[i]+=1
        graph[j].append((i))
q=deque()

for i in range(1,n+1):
    if point[i]==0:
        q.append((i))
# 리스트의 경우, 단순히 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에, 리스트의 값을 복제해야 할 때는 deepcopy() 함수를 사용한다.
result=copy.deepcopy(time)

while q:
    now=q.popleft()
    for i in graph[now]:
        result[i]=max(result[i],result[now]+time[i])
        point[i]-=1
        if point[i]==0:
            q.append(i)
for i in range(1,n+1):
    print(result[i])