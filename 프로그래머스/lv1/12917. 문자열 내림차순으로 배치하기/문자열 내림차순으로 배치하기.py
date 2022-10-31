def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse=True)
    print(s)
    for i in s:
        answer += i
    return answer