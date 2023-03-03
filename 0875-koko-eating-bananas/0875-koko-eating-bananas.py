class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
           
        
        
        start = 1
        
        end = max(piles)
        
        ans = 0
        
        while start <= end :
            
            mid = start + (end - start) // 2
            
            
            if self.getHour(piles , mid , h)  :
                
                ans = mid 
                
                end = mid - 1
                
            else :
                
                start = mid  + 1
          
            
        return ans
        
        
    def getHour(self , piles, speed ,h ):

        count_turn = 0


        for banana in piles:

            count_turn += banana // speed 

            if banana % speed:

                count_turn += 1
        return count_turn <= h
        
        
        
        
        
                
            