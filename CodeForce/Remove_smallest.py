def sol():
    t = int(input())
    
    for _ in range(t):
        
        len_num = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort()
        isvalid = "YES"
        for i in range(len_num-1):
            if nums[i+1]-nums[i]>1:
                isvalid = "NO"
                break
        print(isvalid)   
sol()
            