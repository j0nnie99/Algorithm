def solution(quiz):
    answer = []
    arr = []
    for i in quiz:
        i = i.split()
        arr.append(i)
    for j in arr:
        if j[1] == '+':
            sum = int(j[0]) + int(j[2])
            if sum == int(j[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            diff = int(j[0]) - int(j[2])
            if diff == int(j[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer