class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        arr = [0 for _ in range(len(nums))]
        
        nums = [(nums[i] , i) for i in range(len(nums))]
        
        count = {nums[i] :0 for i in range(len(nums))}
        
        # print(count)
        
        self.MergeSort(0 , len(nums) - 1, nums , count )
        
        for i , val in enumerate(count.values()):
            arr[i] = val
        
        return arr
        
        
        
        
    
    
    def MergeSort(self , left , right , nums , count):
        
        if left == right :
            
            return [nums[left]]
        
        
        mid = left + (right - left ) // 2
        
        
        leftHalf = self.MergeSort(left, mid ,nums, count )
        rightHalf = self.MergeSort(mid + 1, right , nums ,count)
        
        
        return self.Merge(leftHalf , rightHalf, nums, count)
    
    
    def Merge(self , leftHalf , rightHalf ,nums , count ): 
        
        
        arr = []
        
        left = 0
        
        right = 0 
        
        
        
        while left < len(leftHalf) and right < len(rightHalf):
            # print(leftHalf , rightHalf)
            if leftHalf[left][0] <= rightHalf[right][0]:
                
                arr.append(leftHalf[left])
                
                count[leftHalf[left]] += right
                
                left += 1
                
            else:
                
                arr.append(rightHalf[right])
                
                right += 1
                
                
        
        
        while left < len(leftHalf):
            
            arr.append(leftHalf[left])
            
            count[leftHalf[left]] += right
            
            left += 1
        while right < len(rightHalf):
            arr.append(rightHalf[right])
            right += 1
            
        return arr
        
        
        