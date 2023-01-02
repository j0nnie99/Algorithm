def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    for i in list(my_string):
        answer += i
    return answer