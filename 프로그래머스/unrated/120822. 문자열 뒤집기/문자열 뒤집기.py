def solution(my_string):
    answer = ''
    tmp = list(my_string)
    tmp.reverse()
    for i in tmp:
        answer += i
    return answer