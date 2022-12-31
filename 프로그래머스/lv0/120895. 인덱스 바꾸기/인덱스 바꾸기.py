def solution(my_string, num1, num2):
    answer = ''
    tmp = my_string
    tmp = list(tmp)
    my_string = list(my_string)
    
    tmp[num1] = my_string[num2]
    tmp[num2] = my_string[num1]
    
    for i in tmp:
        answer += i
        
    print(answer)
    
    return answer