def sol():
    bracket = list(input())
    
    num_sub_str = 0
    
    left = []
    right = []
    
    index = []
    
    for i in range(len(bracket)):
        if bracket[i] == "(":
            left.append((bracket[i],i))
        else:
            right.append((bracket[i],i))
    
    l = 0 
    r = 0
    
    index = []
    
    while l<len(left) and r < len(right):
        
        if left[l][1]<right[r][1]:
            index.append((left[l][1]+1,right[r][1]+1))
        l+=1
        r+=1
    print(1)
        
            
        
    
    
    
sol()