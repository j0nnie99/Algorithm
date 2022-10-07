def solution(my_string, n):
    answer = ''
    tmp = list(my_string)
    for i in my_string:
        answer += (i * n)
    return answer