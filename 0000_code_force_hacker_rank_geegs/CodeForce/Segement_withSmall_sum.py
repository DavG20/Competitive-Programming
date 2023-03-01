def solution():
    
    length , num = list(map(int, input().split()))

    nums = list(map(int, input().split()))
    
    max_len = 0
    
    left = 0
    
    windows = 0
    
    
    
    for right in range(length):
        
        windows += nums [ right]
        
        while windows > num:
            windows -= nums [left]
            
            left += 1
        max_len = max(max_len, right - left + 1)
        
        
    
    # for i in range(length):
    #     sum_ = nums[i]
         
    #     j = i + 1
        
    #     while j < length and sum_ <= num :
    #         sum_ += nums[ j]
            
            
            
    #         if sum_ <= num:
    #             max_len = max(max_len , j - i + 1)
    #         j += 1
            
    print(max_len)
solution()