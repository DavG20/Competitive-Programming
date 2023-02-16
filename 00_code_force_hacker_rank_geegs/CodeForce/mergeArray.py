def sol():
    n , m = list(map(int, input().split()))
    
    num1  = list(map(int, input().split()))
    
    num2 = list(map(int, input().split()))
    
    
   
    
    left = 0 
    
    right = 0 
    
    answer = []
    
    while left < n  and right < m:
        if num1[left] < num2[right]:
            answer.append(num1[left])
            left += 1
        else:
            answer.append(num2[right])
            right += 1
    while left < n :
        answer.append(num1[left])
        left += 1
        
    while right < m :
        answer.append(num2[right])
        
        right += 1
    print(*answer)
sol()
            
             
    
    