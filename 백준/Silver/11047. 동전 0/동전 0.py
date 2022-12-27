n, k = map(int, input().split())
arr = []
answer = 0

# 동전의 종류를 담은 배열 생성
for i in range(0, n):
    tmp = int(input())
    arr.append(tmp)

# 배열 역순으로 나누어 보며 동전의 개수 구하기
for i in arr[::-1]: 
    if i <= k:
        answer += k // i
        k %= i
    else:
        continue

print(answer)