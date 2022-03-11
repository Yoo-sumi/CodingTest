s="ababcdcdababcdcd"
s="aabbaccc"
s="abcabcdede"
s="abcabcabcabcdededededede"
s="xababcdcdababcdcd"
def solution(s):
    minn=len(s)
    for i in range(1,len(s)//2+1):
        count=1
        strr=""
        for j in range(i,i*(len(s)//i),i):
            if s[j:j+i]==s[j-i:j]:
                count+=1
            else:
                if count==1:
                    strr+=s[j-i:j]
                    continue
                strr+=str(count)+s[j-i:j]
                count=1
        if j!=len(s):
            if count==1:
                strr+=s[j:]
            else:
                strr+=str(count)+s[j:]
        minn=min(minn,len(strr))

    return minn

print(solution(s))