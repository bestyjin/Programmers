def solution(strings, n):
    answer = []
    sorting = []
    same = []
    for word in strings:
        sorting.append([word[n],word])
    sorting = sorted(sorting, key=lambda x: x[0])
    for index, word in enumerate(sorting):
        if len(same) != 0:
            if sorting[index-1][0] == word[0]:
                same.append(word[1])                
            else:
                same.sort()
                answer += same
                same=[]
                same.append(word[1])
        else:
            same.append(word[1])
            
        if index == len(sorting)-1:
            same.sort()
            answer += same
    return answer