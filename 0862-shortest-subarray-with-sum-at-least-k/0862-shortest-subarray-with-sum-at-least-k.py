class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
        
        
        prefSum = [0]
        
        
        #calculate pref_sum 
        
        for num  in nums :
            
            prefSum.append(prefSum[-1] + num)
        
        ans = n + 1  
        
        
        mono_que = collections.deque()
        
        
        for indx , pref in enumerate(prefSum):
            
            #keep increasing
            
            while mono_que and pref <= prefSum[mono_que[-1]]:
                
                
                mono_que.pop()
                
            while  mono_que and pref - prefSum [mono_que[0]] >= k:
                
                
                ans = min(ans , indx - mono_que.popleft())
            
            mono_que.append(indx)
            
        return ans if ans < n + 1 else -1
                
                
        
        
        
        