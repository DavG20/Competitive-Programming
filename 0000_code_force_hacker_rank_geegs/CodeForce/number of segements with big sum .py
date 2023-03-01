length , s = list(map(int, input().split()))

array  =  list(map(int, input().split()))

ans = 0

left = 0

sum_ = 0

for right in range(length):
    
    sum_ += array[right]
    
    while sum_ >= s:
        
        ans +=  (length  -  right)
        
        sum_ -= array[left]
        
        left += 1
print(ans)
    
    
    
    
    