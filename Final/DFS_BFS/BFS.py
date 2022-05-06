from collections import deque
def solution():
    graph=[
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    q=deque()
    flag=[]
    q.append(1)
    flag.append(1)
    while q:
        now=q.popleft()
        print(now,end=" ")
        for i in graph[now]:
            if not i in flag:
                q.append(i)
                flag.append(i)
solution()