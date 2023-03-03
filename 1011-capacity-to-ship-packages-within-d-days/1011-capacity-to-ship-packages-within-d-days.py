class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        
        start = max(weights)
        
        # if sum(weights) % days:
        #     start += 1
        
        end = sum(weights)
        
        ans  = 0
        
        while start <= end :
            
            max_cap = start + (end - start) // 2
            
            if self.getDays(weights , max_cap , days) < days:
                
                ans = max_cap
                
                end = max_cap - 1
            elif self.getDays(weights , max_cap ,days) >= days:
                
                start = max_cap + 1
                
           
                
        return ans
    
    
    
    
    def getDays(self, weights , max_cap , days ):
        
        prefSum = 0
        
        count = 0
        
        for weight in weights:             
            
            
                
            if prefSum + weight <= max_cap:
                
                
                
                prefSum += weight 
                
            else:
                count += 1
                prefSum = weight
            
            # print(max_cap , prefSum)
            
     
        return count 
        
        
        