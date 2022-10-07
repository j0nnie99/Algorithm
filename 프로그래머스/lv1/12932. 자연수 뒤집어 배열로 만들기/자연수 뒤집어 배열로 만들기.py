def solution(n):
    answer = []
    tmp = list(str(n))
    tmp.reverse()
    for i in tmp:
        answer.append(int(i))
    return answer