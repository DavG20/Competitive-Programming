def sol():
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    sereja = []
    
    dima = []
    
    count = 0
    
    while nums:
        
        max_ = max(nums[0],nums[-1])
        
        if nums[0] == max_:
            nums.pop(0)
        else:
            nums.pop(len(nums)-1)
        if count%2==0:
            sereja.append(max_)
        else:
            dima.append(max_)
        count+=1
    print(sum(sereja), sum(dima))
        
            
sol()
    
    