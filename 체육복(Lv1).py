def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    lost = list(lost_set-reserve_set)
    reserve = list(reserve_set-lost_set)
    for i,k in enumerate(reserve):
        if (k-1) in lost:
            lost.remove(k-1)
        elif (k+1) in lost:
            lost.remove(k+1)
        
    return n-len(lost)