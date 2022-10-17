def solution(numbers, k):
    answer = 0
    n = 0
    # 0 = (0 + 2) % 4
    # 1 = ((0 + 2) + 2) % 4
    # 2 = ((0 + 2) + 2) + 2
    n = (2 * (k-1)) % len(numbers)
    answer = numbers[n]
    return answer