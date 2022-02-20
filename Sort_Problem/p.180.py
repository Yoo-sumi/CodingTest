n=2
array=[('홍길동',95),('이순신',77)]
def setting(data):
    return data[1]
array.sort(key=lambda x: x[1])
for i in array:
    print(i[0],end=" ")