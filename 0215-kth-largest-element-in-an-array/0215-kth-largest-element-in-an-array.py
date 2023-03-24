class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        return self.getKth(nums ,k, 0 , len(nums) - 1)
    
    
    
    
    def getKth(self , nums , k ,  left , right  ):
        
        if left == right :
            return nums[left]
        
        pivot = left 
        
        w = pivot
        
        r = pivot + 1
        
    
        
        while r <= right :
            
            if nums[pivot] > nums[r] :
                w += 1
                nums[r], nums[w] = nums[w] , nums[r]
                
                
            r += 1
        if nums[pivot] > nums[w  ]:
            nums[pivot] , nums[w  ] = nums[w ] , nums[pivot]
        
        # print(nums ,pivot, w, r ,right)
        
        if len(nums) - k == w :
            
            
            
            return nums[ w ]
        
        if len(nums) - k < w :
            
            return self.getKth(nums , k , left , w - 1)
        else:
            return self.getKth(nums , k , w + 1  , right )
        