def solution(n):
    answer = 0
    i = 1
    while True:
        if (i * i) == n:
            answer = (i + 1) ** 2
            break
        elif i >= n:
            answer = -1
            break
        else:
            i += 1
            continue
    return answer