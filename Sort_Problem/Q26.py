import heapq
n=3
card=[10,20,40]

heap=[]
for i in card:
    heapq.heappush(heap,i)
result=0
if len(heap)==1:
    result=heapq.heappop(heap)
else:
    while len(heap)!=1:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)

        result+=(a+b)
        heapq.heappush(heap,a+b)

print(result)