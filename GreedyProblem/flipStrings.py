s=str(input())

count_zero=0
count_one=0
flag=None

def count(flag,count_zero,count_one):
    if int(s[0])==0:
        count_zero+=1
        flag=False
    else:
        count_one+=1
        flag=True
    for i in range(1,len(s)):
        if int(s[i])==0 and flag==True:
            count_zero+=1
            flag=False
        elif int(s[i])==1 and flag==False:
            count_one+=1
            flag=True
    return min(count_zero,count_one)
print(count(flag,count_zero,count_one))