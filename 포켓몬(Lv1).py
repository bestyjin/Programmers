from collections import Counter
def solution(nums):
    answer = 0
    answer = min(len(Counter(nums).keys()),len(nums)/2)
    return answer