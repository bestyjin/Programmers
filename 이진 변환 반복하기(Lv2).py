def solution(s):
    answer = []
    count = 0
    zero = 0
    while int(s) != 1:
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
        count+=1
    answer = [count,zero]

    return answer