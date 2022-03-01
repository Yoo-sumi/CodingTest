n=20
d=[0]*(n+1)
d[1]=1
index2=index3=index5=d[1]
next2,next3,next5=2,3,5

for i in range(2,n+1):
    d[i]=min(next2,next3,next5)
    if d[i]==next2:
        index2+=1
        next2=d[index2]*2
    if d[i]==next3:
        index3+=1
        next3=d[index3]*3
    if d[i]==next5:
        index5+=1
        next5=d[index5]*5

print(d)
print(d[n])

#[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
#[0, 1, 2, 3, 4]
#[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12]