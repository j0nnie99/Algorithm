def solution(box, n):
    answer = 1
    tmp = 1
    for i in range(0, len(box)):
        tmp = box[i] // n
        answer *= tmp
    return answer