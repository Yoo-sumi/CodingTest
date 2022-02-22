words=["frodo","front","frost","frozen","frame","kakao"]
queries=["fro??","????o","fr???","fro???","pro?"]
def fist(target,words):
    target=target.replace("?","a")
    start=0
    end=len(target)-1
    while(start<=end):
        mid=(start+end)//2
        if target<=words[mid] and (words[mid-1]<target or mid==0):
            return mid
        elif target>words[mid]:
            start=mid+1
        else:
            end=mid-1
def last(target,words):
    target=target.replace("?","z")
    start=0
    end=len(target)-1
    while(start<=end):
        mid=(start+end)//2
        if target>=words[mid] and (words[mid+1]>target or mid==len(words)-1):
            return mid
        elif target>words[mid]:
            start=mid+1
        else:
            end=mid-1
def re(target,words):
    sum=0
    count=len(target)-target.count('?')
    for i in words:
        if len(i)==len(target) and i[-count:]==target[-count:]:
            sum+=1
    return sum
def solution(words, queries):
    answer=[]
    words.sort()
    for j in queries:
        if j[0]=="?":
            answer.append(re(j,words))
            continue
        firstt=fist(j,words)
        if firstt==None:
            answer.append(0)
            continue
        lastt=last(j,words)
        result_arr=words[firstt:(lastt+1)]
        count=0
        for i in result_arr:
            if len(i)!=len(j):
                count+=1
        answer.append(len(result_arr)-count)
    return answer
print(solution(words,queries))