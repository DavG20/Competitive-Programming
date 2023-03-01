

t = int(input())


for _ in range(t):
    
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    pos = []
    
    for i , num in enumerate(nums):
        
        if num > 0 or i == n - 1:
            pos.append(i)
            
    ans = sum(nums[:-1])
    
    for i in range(len(pos) - 1):
        ans += pos[i+1] - pos[i] - 1
    print(ans)
    
    

            