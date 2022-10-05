def isPrime(number):
    if number==1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i ==0:
            return False
        
    return True
    
from itertools import combinations    
def solution(nums):
    answer = 0
    
    for i in combinations(nums,3):
        if isPrime(sum(i)):
            answer+=1
            
    return answer