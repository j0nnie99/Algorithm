def solution(age):
    answer = ''
    tmp = list(str(age))
    for i in tmp:
        answer += chr(97 + int(i))
    return answer