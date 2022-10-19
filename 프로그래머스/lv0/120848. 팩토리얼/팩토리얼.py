def solution(n):
    answer = 0
    tmp = 1
    i = 1
    while True:
        tmp *= i
        if tmp > n:
            answer = i - 1
            break
        i += 1
    return answer