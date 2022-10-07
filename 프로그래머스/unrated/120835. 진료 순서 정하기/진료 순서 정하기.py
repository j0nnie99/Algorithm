def solution(emergency):
    answer = []
    
    print(emergency)
    # 내림차순 정렬
    tmp = list(emergency)
    tmp.sort(reverse = True)
    
    for i in emergency:
        answer.append(tmp.index(i) + 1)
        
    return answer