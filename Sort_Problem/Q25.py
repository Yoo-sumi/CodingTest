n=5
stages=[2,1,2,6,2,4,3,3]

def solution(N,stages):
    answer=[]
    yet=0
    su=len(stages)
    for i in range(1,N+1):
        su-=yet
        yet=stages.count(i)
        if su==0:
            answer.append((0,i))
        else:
            answer.append((yet/su,i))
    answer.sort(key=lambda x:(-x[0],x[1]))

    answer=[i[1] for i in answer]
    return answer
print(solution(n,stages))
