Set_A=set(input().split())
len_A=len(Set_A)
ans=True
n=int(input())
for i in range(n):
    N=set(input().split())
    for num in N:
        if num not in Set_A or len(N)==len_A:
            ans=False
            break
print(ans)