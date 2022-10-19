from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        first = prices.popleft()
        count = 0
        for price in prices:
            count+=1
            if first>price:
                break
        answer.append(count)
    return answer