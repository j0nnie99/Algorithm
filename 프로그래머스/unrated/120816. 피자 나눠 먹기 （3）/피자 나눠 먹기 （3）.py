def solution(slice, n):
    answer = 0
    # 사람 수가 조각 수보다 많으면 (최소 2판)
    if (n > slice):
        # 남는 조각 없이 나눌 경우
        if (n % slice) == 0:
            answer =  n // slice
        else:
            answer = (n // slice) + 1
    # 사람 수 < 조각 수 (1판)
    else:
        answer = 1
    return answer