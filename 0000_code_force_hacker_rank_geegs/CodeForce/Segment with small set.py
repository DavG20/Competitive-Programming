
length , s = list(map(int, input().split()))

arr = list(map(int, input().split()))


left = 0

ans = 0 

unique = {}

for right in range(length):
    
    unique[arr[right]] = unique.get(arr[right],0) + 1
    
    while len(unique) > s:
        
        unique[arr[left]] -= 1
        if unique[arr[left]] == 0:
            unique.pop(arr[left])
        left += 1
    ans += right - left + 1
print(ans)
    
    