def solution(lottos, win_nums):
    count = 0
    zero = 0
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for i, n in enumerate(lottos):
        if n == 0:
            zero += 1
            continue
        for j, m in enumerate(win_nums):
            if n == m:
                count+=1
    
    return [rank[count+zero],rank[count]]