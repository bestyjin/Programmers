def solution(s):
    count = 0
    zero = 0
    
    while s!='1':
        zero+=len(s)
        s=s.replace('0','')
        zero-=len(s)
        c = len(s)
        s=bin(c)[2:]
        count+=1
    
    return [count,zero]