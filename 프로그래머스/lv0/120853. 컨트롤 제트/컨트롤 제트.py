def solution(s):
    answer = 0
    s = s.split(' ')
    bf = 0
    for i in s:
        if i == "Z":
            answer -= int(bf)
            bf = 0
        else:
            answer += int(i)
            bf = i
    return answer