def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    tmp = list(my_string)
    
    for i in range(len(my_string)):
        if my_string[i] in vowels:
            tmp.remove(my_string[i])
    
    for j in tmp:
        answer += j

    return answer