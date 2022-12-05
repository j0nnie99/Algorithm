def solution(sides):
    answer = 0
    max_side = max(sides)
    shorts = sides
    shorts.remove(max_side)
    if max_side < (shorts[0] + shorts[1]):
        return 1
    else:
        return 2
    return answer