def solution(n):
    answer = 0
    bigger = n+1
    while n < bigger:
        if bin(n).count('1') == bin(bigger).count('1'):
            break
        bigger+=1
    return bigger