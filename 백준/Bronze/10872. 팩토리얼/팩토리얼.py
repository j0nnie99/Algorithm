n = int(input())
answer = 1

if n > 0:
    for i in range(n, 1, -1):
        answer *= i

print(answer)