def solution(s):
    answer = ''
    s = list(map(int, s.split(" ")))
    print(max(s))
    print(min(s))
    answer += str(min(s))
    answer += (" " + str(max(s)))

    return answer