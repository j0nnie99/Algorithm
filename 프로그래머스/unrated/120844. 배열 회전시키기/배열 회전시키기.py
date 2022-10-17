def solution(numbers, direction):
    answer = []
    tmp = []
    if direction == "left":        
        tmp = numbers[1:]
        tmp.append(numbers[0])
        answer = tmp
    elif direction == "right":        
        tmp = numbers[:-1]
        tmp.insert(0, numbers[-1])
        answer = tmp
        
    return answer