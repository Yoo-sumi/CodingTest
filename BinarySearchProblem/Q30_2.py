from bisect import bisect_left,bisect_right
words=["frodo","front","frost","frozen","frame","kakao"]
queries=["fro??","????o","fr???","fro???","pro?"]
def count_by_range(a,left,right):
    right_index=bisect_right(a,right)
    left_index=bisect_left(a,left)
    return right_index-left_index
def solution(words, queries):
    array=[[] for _ in range(10001)]
    reverse_array=[[] for _ in range(10001)]
    for i in words:
        array[len(i)].append(i)
        reverse_array[len(i)].append(i[::-1])
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
    answer = []
    for i in queries:
        if i[0]!='?':
            answer.append(count_by_range(array[len(i)],i.replace('?','a'),i.replace('?','z')))
        else:
            answer.append(count_by_range(reverse_array[len(i)],i[::-1].replace('?','a'),i[::-1].replace('?','z')))
    return answer

print(solution(words,queries))