def solution(my_string):
    answer = 0
    numbers= ['0','1','2','3','4','5','6','7','8','9']
    ms = list(my_string)
    for i in ms:
        if i in numbers:
            answer += int(i)
    return answer