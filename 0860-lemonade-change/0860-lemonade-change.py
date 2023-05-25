class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_five = 0 
        
        num_ten = 0
        
        num_twenty = 0
        
        
                
        for num in bills:
            print(num )
            if num == 5 :
                
                num_five += 1
                
            if num == 10 :
                if num_five:
                    
                    num_five -= 1

                    num_ten += 1
                else:
                    return False
                
            if num == 20:
                
                if num_ten and num_five :
                    num_five -= 1
                    num_ten -= 1
                    num_twenty += 1
                else:
                    if num_five >= 3:
                        num_five -= 3
                    else:
                        return False
                    # return False
        return True
                    
                

            
        