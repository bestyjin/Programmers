def solution(n):
    ten = n
    b = 3
    result=[]
    while ten:
        result.append(str(ten%b))
        ten //= b
    
    result=int(''.join(result),3)
    return result