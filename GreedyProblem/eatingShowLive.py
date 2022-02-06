# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    length=len(food_times)
    sum_value=0
    previous=0
    while sum_value+(length*(q[0][0]-previous))<=k:
        now=heapq.heappop(q)[0]
        sum_value+=length*(now-previous)
        previous=now
        length-=1
    result=sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]