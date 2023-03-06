class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        arr = [0 for i in range(1001)]
        
        
        for trip in  trips:
            
            if trip[-1] + 2 < len(arr):
                
                arr[trip[-1] + 1] -= trip[0]
                
            arr[trip[1] + 1] += trip[0]
        
        
        
        
        for i in range(1,len(arr)):
            
            arr[i] = arr[i - 1] + arr[i]
            
            
        
        
        return capacity >= max(arr)
            
            
        
        
                
        
        