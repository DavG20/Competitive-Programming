def sol():
    
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    index = []
    
    for i in range(n):
        target = i
        for j in range(i+1,n):
            if nums[target]>nums[j]:
                target = j
        if target != i:
            nums[target], nums[i] = nums[i] , nums[target]
            index.append((i,target))
            
    print(len(index))
    
    for i , j in index:
        print(i , j )
sol()
        
            
            
            