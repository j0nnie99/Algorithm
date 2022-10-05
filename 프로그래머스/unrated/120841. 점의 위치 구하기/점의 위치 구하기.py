def solution(dot):
    answer = 0
    # x,y 음수 양수 판별용
    xx = 0 
    yy = 0
    
    # 결과값 배열
    xy = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    
    # 입력값 양음수 판단
    if dot[0] > 0:
        xx = 1
    else:
        xx = -1
        
    if dot[1] > 0:
        yy = 1
    else:
        yy = -1
        
    answer = xy.index([xx, yy]) + 1
    print(xx, yy)
        
    return answer