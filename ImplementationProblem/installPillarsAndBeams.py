n=5
#build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
def judge(answer):
    for xx,yy,aa in answer:
        if aa==0:
            if yy==0 or [xx,yy-1,0] in answer or [xx-1,yy,1] in answer or [xx,yy,1] in answer:
                continue
            return False
        elif aa==1:
            if ([xx-1,yy,1] in answer and [xx+1,yy,1] in answer) or [xx,yy-1,0] in answer or [xx+1,yy-1,0] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer=[]
    for x,y,a,b in build_frame:
        if b==1: # 설치
            answer.append([x,y,a])
            if not judge(answer):
                answer.remove([x,y,a])
        elif b==0: #삭제
            answer.remove([x,y,a])
            if not judge(answer):
                answer.append([x,y,a])
    answer.sort()
    return answer


print(solution(n,build_frame))