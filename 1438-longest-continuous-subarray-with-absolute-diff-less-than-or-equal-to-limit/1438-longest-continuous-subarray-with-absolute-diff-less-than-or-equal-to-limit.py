class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        min_q = deque()
        
        max_q = deque()
        
        
        max_size , left =  0 , 0 

        for i in range(len(nums)):
            
            
            while min_q and min_q[-1] > nums[i]:
                
                min_q.pop()
                
            min_q.append(nums[i])
            
            
            while max_q and max_q[-1] < nums[i]:
                
                max_q.pop()
            
            max_q.append(nums[i])
            
            
            
            while  max_q[0] - min_q[0] > limit:
                
                val = nums[left]
                
                if val == min_q[0] :
                    
                    min_q.popleft()
                    
                if val == max_q[0] :
                    
                    max_q.popleft()
                    
                left += 1
            max_size = max(max_size , i - left + 1)
        return max_size 
    
                    
                    
                    
                    
                    
            
            
        
        
        