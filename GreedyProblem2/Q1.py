n=5
array=[2,3,1,2,2]
count=0
result=0
array.sort()
for i in array:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)