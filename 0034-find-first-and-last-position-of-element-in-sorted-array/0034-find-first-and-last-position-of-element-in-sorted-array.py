class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        ans = [-1 , -1 ]
        
        
        ans[0] = self.getRange(nums ,target , False )
        
        ans[1] = self.getRange(nums ,target, True)
      
                
        
        return ans
        
    def getRange(self, nums , target ,isStartFound = True):
        
        start = 0 
        
        end = len(nums) - 1
        
        
        last = -1
    
        
        while start <= end :
            
            mid = start + (end - start )// 2
            
            if nums[mid] <  target :
                
                start = mid + 1                
            
            elif nums[mid] >  target : 
                
                end = mid - 1 
            
        
            else:
                
                last = mid
                
                if isStartFound:
                    
                    start = mid +  1
                    
                else:
                    end = mid - 1
                
        return last
                
                