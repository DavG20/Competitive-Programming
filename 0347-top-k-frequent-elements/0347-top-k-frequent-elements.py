class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        Count_Freq = Counter(nums)
        
        print(list(Count_Freq.items()))
        
        ans = (self.Quick_Select(list(Count_Freq.items()), 0 , len(Count_Freq) - 1 , k))
        
        arr = []
        
        for i in range(k):
            print(ans)
            arr.append(ans[i][0])
            
        return arr
            
            
            
        
        
    
    def Quick_Select(self , nums , left , right , k):
        
    
        
        pivot = left 
        
        w = pivot 
        
        r = pivot 
        
        while r <= right :
           
            if nums[pivot][1] > nums[r][1] :
            
                w += 1
                
                nums[w] , nums[r] = nums[r] ,nums[w]
                                
                
            r += 1
            
        
        
        nums[pivot ] , nums[w] = nums[w] , nums[pivot]
        
        
        
        if len(nums) - k == w :
            
            return nums[w:]
                        
        if len(nums) - k < w :
            
            return self.Quick_Select(nums , left , w - 1, k)
        
        else:
            
            return self.Quick_Select(nums , w + 1 , right, k)
            
            
        
        