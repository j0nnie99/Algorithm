s = input()
lst = list(s)
cnt1 = 0
cnt2 = 0

if lst[0] == '0':
    cnt2 += 1
else:
    cnt1 += 1

for i in range(0, len(lst)):
    if lst[i] != lst[i-1]:
        if lst[i] == '0':
            cnt1 += 1
        else:
            cnt2 += 1
    else:
        continue

print(min(cnt1, cnt2))