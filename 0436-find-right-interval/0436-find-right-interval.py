class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        dicts = { tuple(intrv) : i for i , intrv  in enumerate(intervals)}
        
        
        ans = [-1] * len(intervals)
        
        
        intervals.sort()
        
        flag = False
        
        last_mid = 0
        
        for interval in intervals:
            
            start = 0 
            
            end = len(intervals) - 1
            
            
            while start <= end :

                mid = start + (end - start) // 2
                
                
                if intervals[mid][0] == interval[1]:
                    
                    ans[dicts[tuple(interval)]] = dicts[tuple(intervals[mid])]
                    
                    
                    flag = False
                    
                    break
                    
                elif intervals[mid][0] > interval[1] :
                    
                    last_mid = mid
                    
                    flag = True
                     
                    end = mid  - 1
                else:
                    start = mid + 1
            if flag:
                ans[dicts[tuple(interval)]] = dicts[tuple(intervals[last_mid])]
                
                flag = False
                    
        return ans
                
        
        
        