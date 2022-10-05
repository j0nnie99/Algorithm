def solution(n):
    answer = 0
    lst = []
    lst = list(str(n))
    for i in lst:
        answer += int(i)
    return answer