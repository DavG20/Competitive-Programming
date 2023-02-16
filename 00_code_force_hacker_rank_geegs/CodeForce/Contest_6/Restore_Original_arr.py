def sol():
    
    t = int(input())
    
    for t in range(t):
        
        len_num = int(input())
        
        nums = list(map(int, input().split()))
        
        mod_arr = []
        left = 0
        right = len_num - 1
        for i in range(len_num):
            if i%2==0 :
                mod_arr.append(nums[left])
                left += 1
            else:
                mod_arr.append(nums[right])
                right -= 1
        print(*(mod_arr))
sol()
            