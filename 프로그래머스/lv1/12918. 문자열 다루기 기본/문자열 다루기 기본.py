def solution(s):
    answer = True
    s = list(s)
    print(len(s))

    if (len(s) == 4) | (len(s) == 6):
        print(len(s))
        for i in s:
            if i.isdigit() == False:
                # print(i, "는 문자!")
                answer = False
    else:
        answer = False
    return answer