def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    for i in range(len(s)):
        if i == 0:
            answer.append(int(s[i]))
        else:
            new_s = s[i].split(',')
            for j in new_s:
                if not int(j) in answer:
                    answer.append(int(j))
                    break
    return answer