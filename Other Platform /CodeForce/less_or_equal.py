def sol():
    n , k = list(map(int, input().split()))
    
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    nums = [1] + nums + [float('inf')]
    
    if nums[k+1] - nums[k] > 0:
        print(nums[k])
    else:
        print(-1)
sol()
        