def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]*(1+len(answers)//5)
    student2 = [2,1,2,3,2,4,2,5]*(1+len(answers)//8)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(1+len(answers)//10)
    students = {1:0,2:0,3:0}
    
    for i, n in enumerate(answers):
        if student1[i] == n:
            students[1]+=1
        if student2[i] == n:
            students[2]+=1
        if student3[i] == n:
            students[3]+=1
            
    for i in students:
        if len(answer) == 0:
            answer.append(i)
        elif students[answer[-1]] < students[i]:
            answer = []
            answer.append(i)
        elif students[answer[-1]] == students[i]:
            answer.append(i)
        
    return sorted(answer)