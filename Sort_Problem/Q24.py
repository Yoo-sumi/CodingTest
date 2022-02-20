n=4
home=[5,1,7,9]
'''sum_array=[]
for i in home:
    sum=0
    for j in home:
        sum+=abs(i-j)
    sum_array.append((sum,i))
sum_array.sort(key=lambda x: (x[0],x[1]))
print(sum_array[0][0])'''
home.sort()
print(home[(n//2)-1])
