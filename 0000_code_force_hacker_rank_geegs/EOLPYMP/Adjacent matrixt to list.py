from collections import defaultdict
n = int(input())

adjc_matrix = []

for _ in range(n):

    adjc_matrix.append(list(map(int, input().split())))


adj_List = defaultdict(list)

for i in range(n):
    for j in range(n):
        if adjc_matrix[i][j]:
            adj_List[i+1].append(j + 1)
for i in range(1,n + 1):
    print(len(adj_List[i]) , * adj_List[i])