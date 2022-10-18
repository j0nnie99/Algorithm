def solution(numbers):
    answer = 1
    numbers.sort()
    n = len(numbers)
    answer = numbers[n-1] * numbers[n-2]
    return answer