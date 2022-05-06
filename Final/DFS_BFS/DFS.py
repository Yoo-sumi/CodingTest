def dfs(graph,v,flag):
    flag.append(v)
    print(v,end=" ")
    for i in graph[v]:
        if not i in flag:
            dfs(graph,i,flag)
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
    dfs(graph,1,[])
solution()