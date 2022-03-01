A="sunday"
B="saturday"

array=[[0]*len(B) for _ in range(len(A))]

for i in range(len(B)):
    array[0][i]=i
for i in range(len(A)):
    array[i][0]=i

for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            array[i][j]=min(array[i][j-1],array[i-1][j-1],array[i-1][j])
        else:
            array[i][j]=min(array[i][j-1],array[i-1][j-1],array[i-1][j])+1
print(array[len(A)-1][len(B)-1])
print(array)