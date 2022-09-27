def solution(s):
    answer = ''
    string = list(s.lower())
    string[0] = string[0].upper()
    for i in range(1,len(string)):
        if string[i-1] == ' ':
            string[i] = string[i].upper()    
                   
    return ''.join(string)