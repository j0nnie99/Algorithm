def solution(denum1, num1, denum2, num2):
    answer = []
    tmp = []
    
    # 두 분수의 합을 분자, 분모 순으로 저장 (기약분수X)
    tmp = [(denum1 * num2) + (denum2 * num1), num1 * num2]
    
    # 기약분수로 만들기
    # 2부터 분모/분자 중 작은 수까지 나눠보기
    # 분모 분자가 모두 나누어 떨어질 경우 tmp 값 갱신
    for i in range(min(tmp), 1, -1):
        if (tmp[0] % i == 0) and (tmp[1] % i == 0):
            tmp[0] = tmp[0] / i
            tmp[1] = tmp[1] / i
        else:
            continue
    
    answer.append(tmp[0])
    answer.append(tmp[1])

    
    return answer