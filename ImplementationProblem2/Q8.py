s="K1KA5CB7"
s="AJKDLSI412K4JSJ9D"
str_array=[]
num_sum=0

for i in range(len(s)):
    if 47<ord(s[i])<58:
        num_sum+=int(s[i])
    else:
        str_array.append(s[i])
str_array.sort()
for i in str_array:
    print(i,end="")
print(num_sum)