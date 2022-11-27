def solution(my_string):
    answer = ''
    # my_string = my_string.replace(' ', '')
    my_string = list(dict.fromkeys(my_string))
    for i in my_string:
        answer += i
    return answer