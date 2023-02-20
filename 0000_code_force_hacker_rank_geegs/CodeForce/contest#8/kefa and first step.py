def sol():
    
    n = int(input())
    
    
    nums = list(map(int, input().split()))
    
    max_= 0
    
    left = 0 
    
    right = 0
    
    while left < n:
        count = 0
        while right < n -1:
            if nums [right] <= nums[right+1]:
                count += 1
                right += 1
            else:
                break
        left = right
        right += 1
        max_ = max(max_ , count + 1)
                
        
        
            
    print(max_)    
            
sol()     
                
            