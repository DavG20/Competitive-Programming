from collections import defaultdict


n = int(input())

plane = list(map(int, input().split()))


plane_dict = defaultdict(list)

for i in range(len(plane)):
    plane_dict[i + 1].append(plane[i])
count = 0
last = "NO"

for x , y in plane_dict.items():
    if y[-1]  in plane_dict:
        count += 1
    if count >= 3:
        last = "YES"
        break
print(last)




