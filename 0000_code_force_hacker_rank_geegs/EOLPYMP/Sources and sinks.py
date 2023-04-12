n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

Sink = set(i + 1 for i in range(n))
Source = set(i + 1 for i in range(n))


for i in range(n):
    flage = False

    for j in range(n):
        if matrix[i][j]:
            if Source and j + 1 in Source:
                Source.remove(j + 1)
            if Sink and i + 1 in Sink:
                Sink.remove(i + 1)


print(len(Source), *Source)

print(len(Sink), *Sink)
