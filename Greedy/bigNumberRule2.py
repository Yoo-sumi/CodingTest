n, m, k = map(int, input().split()) #n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 초과횟수
data=list(map(int, input().split()))
sum=0

data.sort()
first=data[n-1]
second=data[n-2]

first_count=int(m/(k+1))*k+m%(k+1)
second_count=m-first_count #m//(k+1)

sum=first_count*first+second_count*second
print(sum)


