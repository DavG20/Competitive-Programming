def sol():
    
    n , m  = list(map(int, input().split()))
    
    num1 = list(map(int, input().split()))
    
    
    num2  =  list(map(int, input().split()))
    
    
    
    num1_pointer  = 0
    
    num2_pointer = 0 
    
    answer = []
    
    while  num1_pointer < n and num2_pointer < m:
        
        if num1[num1_pointer]<num2[num2_pointer]:
            num1_pointer += 1
        else:
            
            answer.append(num1_pointer)
            num2_pointer += 1
    while num2_pointer < m:
        answer.append(num1_pointer)
        num2_pointer += 1
    print(* answer)
    
sol()