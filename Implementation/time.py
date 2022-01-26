n=int(input())
count=0
for i in range(n+1):
    for j in range(60):
        for h in range(60):
            if '3' in str(i)+str(j)+str(h): # 3이 하나라도 포함되는지
                count+=1
print(count)