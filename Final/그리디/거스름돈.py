n=1260
count=0
money=[500,100,50,10]

for i in money:
    if n==0:
        break
    count+=n//i
    n%=i
print(count)