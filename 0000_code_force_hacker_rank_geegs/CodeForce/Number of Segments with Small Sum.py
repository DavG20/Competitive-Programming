length , num = list(map(int, input().split()))

nums = list(map(int, input().split()))

ans = 0

sum_ =0

left  = 0

for right in range(length):
    
    sum_ += nums[right]
    
    while sum_ > num:
        sum_ -= nums[left]
        
        left += 1
    ans += right - left + 1
print(ans)
    
    
    