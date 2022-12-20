from collections import Counter
ans=[]
for i in range(int(input())):
    ans.append(input())
count=Counter(ans)
print(len(count),end="\n")
for num in count.values():
    print(num,end=" ")
    