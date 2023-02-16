def sol(n):
    answer=[]
    for _ in range(n):
        answer.append(list(map(int,input().split())))
    answer.sort(key=lambda x:x[0])
    for i in range(n-1):
        if answer[i][1]>answer[i+1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")
 


n=int(input())

sol(n)
        