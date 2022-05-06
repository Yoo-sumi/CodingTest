n=int(input())
def solution():
    answer=0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                time=str(h)+str(m)+str(s)
                if time.count('3')>0:
                    answer+=1
    return answer
print(solution())