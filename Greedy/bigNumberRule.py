n, m, k = map(int, input().split()) #n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 초과횟수
data=list(map(int, input().split()))
sum=0

data.sort()
first=data[n-1]
second=data[n-2]

for i in range(m):
    if (i+1)%k==0:
        sum+=second #second_max
        continue
    sum+=first #max
print(sum)


