class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        count = {}
        
        
        for num in nums:
            
            self.PrimeFac(num ,count)
        
        print(count)
        return len(count)
        
        
    
    
    
    def PrimeFac(self , num , count):
        
        d = 2 
        
        
        while d * d <= num :
            
            while num % d == 0 :
                
                count[d] =count.get(d , 0) + 1
                
                num //= d
            d += 1
            
        print(num)
        if num > 1:
            count[num] =count.get(num , 0) + 1
            
            
        return count