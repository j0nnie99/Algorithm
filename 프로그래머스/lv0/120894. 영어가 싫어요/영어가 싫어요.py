def solution(numbers):
    answer = numbers
    eng_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    pairs = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven":  7, "eight": 8, "nine": 9}
    for i in eng_numbers:
        if i in answer:
            answer = answer.replace(i, str(pairs[i]))
    answer = int(answer)
    return answer