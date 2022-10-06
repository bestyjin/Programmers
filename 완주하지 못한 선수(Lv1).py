from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    
    return str(list(answer.keys())[0])