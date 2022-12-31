def solution(array, n):
    answer = 0
    diff = 10000
    array.sort(reverse=True)
    for i in array:
        if abs(n - i) <= diff:
            answer = i
            diff = abs(n - i)
    return answer