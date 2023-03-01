class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left  = [1 for _ in range(n)]
        
        right = [1 for _ in range(n)]
        
      
        
        product_arr = []
        
        rev_arr = nums[::-1]
        
        for i in range(1 , n):
            
            left [i] = nums[ i - 1 ] * left[ i - 1 ]
            
        
        
        for i in range(1 , n):
            
            right [i] = right[i - 1] * rev_arr[i - 1]
            
        right = right[:: -1]
        
        for i in range(n):
            
            nums[i] = left[i] * right[i]
            
        return nums
            
            
            
            
        