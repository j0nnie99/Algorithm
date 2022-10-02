def solution(array):
    answer = []
    max_num = 0
    max_num = max(array)
    max_loc = array.index(max_num)
    answer = [max_num, max_loc]
    return answer