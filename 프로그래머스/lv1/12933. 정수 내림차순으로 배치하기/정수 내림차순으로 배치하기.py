def solution(n):
    answer = ''
    tmp = list(str(n))
    tmp.sort(reverse=True)
    for i in tmp:
        answer += str(i)
    answer = int(answer)
    return answer