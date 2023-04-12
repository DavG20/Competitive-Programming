def Raising_bacteria():
    n = int(input())
    count = (n >> 0) & 1
    while n > 0 :

        if (n >> 1) & 1 :
            count += 1
        n >>= 1
    print(count)

    

    
    

        

    # count = 0 

    # while n :
    #     if n % 2 == 0:
    #         n //= 2
    #     else:
    #         count += 1
    #         n //= 2
    
    
            
        
        

Raising_bacteria()