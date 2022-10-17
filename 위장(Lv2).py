def solution(clothes):
    answer = 1
    dictionary = {}
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    
    for key in dictionary.keys():
        answer *= len(dictionary[key])+1
    
    return answer - 1