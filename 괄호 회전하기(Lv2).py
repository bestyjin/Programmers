def check(s):
    stack = []
    for i in s:
        if len(stack) > 0:
            if stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for x in range(len(s)):
        if x == 0:
            new_s = s
        else:
            new_s = s[x:]+s[:x]
        if check(new_s):
            answer+=1
            
    return answer