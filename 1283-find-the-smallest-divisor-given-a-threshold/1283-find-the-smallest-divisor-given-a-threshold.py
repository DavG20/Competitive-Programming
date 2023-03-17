class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        n = len(nums)
          
        
        nums.sort()
        
        
        start = 1
        
        
        end = max(nums)
        
        last = n
        
        while start <= end :
            
            mid = start + (end - start ) // 2
            
            print(sum(self.getDiv(nums ,mid)),mid)
            
            if sum(self.getDiv(nums ,mid)) > threshold :
                
                start = mid + 1
                
            elif sum(self.getDiv(nums ,mid)) <= threshold :
                
                last = mid 
                
                end = mid - 1
#             else:
                
#                 return mid 
            
        return last
            
    def getDiv(self, nums , divisor)  :
        
        arr = []
        
        for num in nums :
            
            arr.append(math.ceil(num / divisor))
        return arr
        
        
        
        
        
        