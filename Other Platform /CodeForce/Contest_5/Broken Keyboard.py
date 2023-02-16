def sol():
    
    n = int(input())
    
    letter_all = []
    
    for _ in range(n):
        
        letters =  list(input())
        
        valid_button = set()
        
        
        
        if len(letters)==1:
            letter_all.append(letters)
            
        else:
            i = 1
            
            while i < len(letters):
                
                if letters[i] != letters[i-1]: 
                    valid_button.add(letters[i-1])
                    i+=1
                else:
                    i+=2
            if letters[-1] != letters[len(letters)-2]:
                valid_button.add(letters[-1])
                
            letter_all.append(sorted(list(valid_button)))
    for letter in letter_all:
        let=""
        for char in letter:
            let+=char
        print(let)
            
sol()
            
        
        