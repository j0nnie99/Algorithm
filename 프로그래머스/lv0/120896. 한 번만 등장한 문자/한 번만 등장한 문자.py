def solution(s):
    answer = ''
    s = list(s)
    alist = []
    
    for i in s:
        if s.count(i) == 1:
            alist.append(i)
    
    alist.sort()
    
    for i in alist:
        answer += i
    return answer