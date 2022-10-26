def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        n = min(arr)
        arr.remove(n)
        answer = arr
    return answer