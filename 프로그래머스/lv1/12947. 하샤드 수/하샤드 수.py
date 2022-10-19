def solution(x):
    answer = True
    sum = 0
    tmp = []
    tmp = list(map(int, str(x)))
    for i in tmp:
        sum += i
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer