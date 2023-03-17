class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        n = len(citations)
        
        
        end = n - 1
        
        start = 0
        
        
        while start <= end :
            
            mid = start + (end - start )// 2
            
            if citations[mid] == n - mid :
                
                return citations[mid]
            
            elif citations[mid] < n - mid :
                
                start = mid + 1
                
            else:
                
                end = mid - 1
                
        return n - start 
        
        