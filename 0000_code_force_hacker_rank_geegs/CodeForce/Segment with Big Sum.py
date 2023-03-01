length , s = list(map(int, input().split()))

nums = list(map(int, input().split()))

sum_  = 0

left = 0 

min_len = float('inf')

for right in range(length):
    sum_ += nums[right]
    # if sum_ >= num:min_len = min(min_len , right - left + 1 )
    while sum_ >= s:
        
        
            
        min_len = min(min_len , right - left + 1 )
            
        sum_ -=  nums[left]
        left += 1
        
        
        
            
if min_len == float('inf'):
    print(-1)
else:
    print(min_len)