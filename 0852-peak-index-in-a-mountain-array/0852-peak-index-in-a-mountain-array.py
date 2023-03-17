class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        # start and end must instantiate by shifting to the right and to the left by one 
        
        
        start = 1
        
        end = len(arr) - 2
        
        
        while start <= end :
            
            mid = start + (end - start ) // 2
            
            # when our array is to the left of the mountain peak
            
            if arr[mid - 1] < arr[mid] < arr[mid + 1] :
                
                start = mid + 1
                
            # to the right of the peak 
            elif  arr[mid - 1] > arr[mid] > arr[mid + 1] :
                
                end = mid - 1
                
            else:
                return mid
            
        