def solution(progresses, speeds):
    answer = []
    a = 0
    b = 0
    days = []
    for i in range(len(progresses)):
        a = 100 - progresses[i]
        b = a // speeds[i]
        if a % speeds[i] != 0:
            b += 1
        days.append(b)
    j = 0
    length = len(days)
    flag = True
    last = False
    while flag:
        count=1
        for k in range(j+1,length):
            if k == length-1:
                flag = False
            if days[j] >= days[k]:
                count+=1
            else:
                j = k
                if flag == False:
                    last = True
                break
        answer.append(count)
        
    if last == True:
        answer.append(1)
        
    return answer