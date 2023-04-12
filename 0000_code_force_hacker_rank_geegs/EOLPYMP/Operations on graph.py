from collections import defaultdict
n = int(input())
opration = int(input())

adjacent = defaultdict(list)

for i in range(opration):
    opr = list(map(int, input().split()))
    

    if len(opr) == 3:
        adjacent[opr[1]].append(opr[2])
        adjacent[opr[2]].append(opr[1])

    else:
    
        print(*adjacent[opr[1]])
# print(adjacent)