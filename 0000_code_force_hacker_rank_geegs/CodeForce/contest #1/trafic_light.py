def sol():
    
    t = int(input())
    
    
    
    
    for _ in range(t):
        
        n , curr_light = input().split()
    
        n = int(n)
        
        
        trafic_light = input()
        
        trafic_light += trafic_light 
        
        
        
        left = 0 
        
        right = 0
        max_ = 0
        while right < n:
            
            
            while right < len(trafic_light) and trafic_light[right]!= curr_light:
                right += 1
            left = right 
            
            while  right < len(trafic_light) and  trafic_light[right] != "g":
                right += 1
        
            max_ = max(max_, right - left)
            right += 1
            
        print(max_)
sol()        
            
    
    
    