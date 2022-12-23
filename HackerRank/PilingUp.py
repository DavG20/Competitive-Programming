def pilingup(d):
    left=0
    right=len(d)-1
    ans=[max(d[0],d[-1])]
    while left<right:
        large=max(d[left],d[right])
        if large>ans[0] and large>ans[-1]:
            return "No"
        if d[left]>=d[right]:
            large=d[left]
            ans.append(d[left])
            left+=1
        if d[left]<d[right]:
            large=d[right]
            ans.append(d[right])
            right-=1
    return "Yes"
for i in range(int(input())):
    n=int(input())
    lists=list(map(int,input().split()))
    print(pilingup(lists))