def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
def solution(n, k):
    answer = 0
    word=""
    while n:            # 숫자를 k진법으로 변환
        word = str(n%k)+word
        n=n//k
        
    word=word.split("0")  # 변환된 숫자를 0을 기준으로 나눈다.

    for i in word:
        if len(i) == 0:
            continue
        elif int(i) < 2:
            continue
        
        if isPrime(int(i)):
            answer+=1
            
    return answer