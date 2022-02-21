n=5
data=[8,3,7,9,2]
m=3
custom=[5,7,9]

count=[0]*(max(data)+1)

for i in data:
    count[i]+=1

for i in custom:
    if count[i]>0:
        print("yes",end=" ")
    else:
        print("no",end=" ")