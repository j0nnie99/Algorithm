n = int(input())
scores = []
answer = 0
for i in range(0, n):
    t = int(input())
    scores.append(t)

for i in range(len(scores)-1, 0, -1):
    if scores[i] <= scores[i-1]:
        tmp = scores[i-1]
        scores[i-1] = scores[i] - 1
        answer += tmp - scores[i-1]

print(answer)
