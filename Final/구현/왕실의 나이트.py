n=str(input())

def solution():
    answer=0
    y=ord(n[0])-97
    x=int(n[1])-1
    dx=[-1,1,-1,1,-2,-2,2,2]
    dy=[2,2,-2,-2,1,-1,1,-1]
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if not 0<=nx<8 or not 0<=ny<8:
            continue
        answer+=1
    return answer

print(solution())