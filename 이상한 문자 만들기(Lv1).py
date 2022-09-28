def solution(s):
    answer = ''
    for i in s.split(' '):
        for index, j in enumerate(i):
            if index%2==0:
                answer+=j.upper()
            else:
                answer+=j.lower()
        answer+=' '
    return answer[:-1]