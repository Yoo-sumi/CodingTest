s="010100110100"
one=zero=False
one_count,zero_count=0,0
for i in s:
    if zero==False and int(i)==0:
        zero_count+=1
        zero=True
        if one==True:
            one=False
    if one==False and int(i)==1:
        one_count+=1
        one=True
        if zero==True:
            zero=False
print(zero_count,one_count)
print(min(zero_count,one_count))