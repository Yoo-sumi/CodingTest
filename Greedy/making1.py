n, k = map(int, input().split())
count=0

def one(n):
    return n-1
def two(n):
    return n/k

while True:
    if n==1:
        break
    if n%k == 0:
        n=two(n)
    else:
        n=one(n)
    count+=1
print(count)