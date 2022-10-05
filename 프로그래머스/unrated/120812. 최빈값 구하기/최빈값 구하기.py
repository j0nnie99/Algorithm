def solution(array):
    answer = 0
    tmp = []
    
    # tmp에 각 수의 빈도값 저장
    for i in array:
        tmp.append(array.count(i))
        
    # 최빈값 = 최빈값의 개수 => 최빈값이 하나
    if max(tmp) == tmp.count(max(tmp)):
        idx = tmp.index(max(tmp))
        answer = array[idx]
    else:
        answer = -1
        
    # # tmp = [1, 1, 2, 2, 3]  
    # # tmp의 최대값 -> 최대 빈도수
    # # 최대값의 개수(3이 최고 빈도 3개)가 array에서 구한 최대 빈도수보다 크면 최대 빈도수
    # if tmp.count(max(tmp)) > max(tmp):
    #     answer = -1
    # else:
    #     answer = tmp.count(max(tmp))
    # # for i in array:
    # #     if array.count(i) > answer:
    # #         answer = array.count(i)
    # #     elif array.count(i) == answer:
    # #         answer = -1
    # #     else:
    # #         continue
    return answer