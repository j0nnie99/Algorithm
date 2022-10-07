def solution(s):
    answer = True
    s = s.lower()

    pc = s.count('p')
    yc = s.count('y')

    if pc != yc :
        answer = False

    return answer