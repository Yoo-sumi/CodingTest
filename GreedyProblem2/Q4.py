n=5
array=[3,2,1,1,9]
array.sort()
target=1
for i in array:
    if target<i:
        break
    target+=i
print(target)