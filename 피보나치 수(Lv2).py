def solution(n):
    answer = 0
    stack = [0]*(n+1)
    stack[0] = 0
    stack[1] = 1
    for i in range(2,n+1):
        stack[i] = stack[i-2] + stack[i-1]

    return stack[n]%1234567