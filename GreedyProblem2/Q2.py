s="02984"
#s="567"
result=int(s[0])
for i in range(1,len(s)):
    if result<=1 or int(s[i])<=1:
        result+=int(s[i])
    else:
        result*=int(s[i])
print(result)