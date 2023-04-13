from collections import Counter
n = int(input())


ans = 0
for i in range(n):

    count = Counter(list(map(int, input().split())))
    ans += count[1]

print(ans // 2)
