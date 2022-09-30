from itertools import combinations
def solution(numbers):
    answer = []
    printList = list(combinations(numbers,2))
    for i in printList:
        answer.append(sum(i))
        
    return sorted(list(set(answer)))