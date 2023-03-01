t = int(input())


for _ in range(t):
    
    length , iter = list(map(int, input().split()))
    
    
    nums = list(map(int,list(input())))
    
    
    for i in range(length):
        
        for j in range(i + 1 , length - 1):
            
            if nums [ j ] ==1:
                
                nums [j + 1] = 1
                
                nums[ j - 1] = 1
    print(nums)