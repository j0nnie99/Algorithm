def solution(n):
    answer = 0

    tmp = list(str(n))
    
    for i in tmp:
        answer += int(i)

    return answer