from itertools import combinations
n,m=map(int,input().split())
array=[]
home=[]
chicken=[]
def measure(arr):
    min_arr=[]
    for x,y in home:
        result=1e9
        for z,h in arr:
            result=min(result,abs(x-z)+abs(y-h))
        min_arr.append(result)
    return sum(min_arr)

for i in range(n):
    array.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j]==1:
            chicken.append((i+1,j+1))
        elif array[i][j]==2:
            home.append((i+1,j+1))

combinates=list(combinations(chicken,m))
sum_arr=[]
for i in combinates:
    sum_arr.append(measure(i))
print(min(sum_arr))