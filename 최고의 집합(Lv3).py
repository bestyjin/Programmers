def solution(n, s):
    if s//n == 0:
        return [-1]
    else:
        answer = [s//n]*n
        if n%s != 0:
            add = s%n
            for i in range(1,len(answer)+1):
                if add == 0:
                    break
                answer[-i] += 1
                add -= 1
        return answer