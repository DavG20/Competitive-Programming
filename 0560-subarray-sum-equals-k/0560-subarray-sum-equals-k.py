class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefSum = [0]
        
        subArr = 0
        
        for num in nums:
            prefSum.append(prefSum[-1] + num)
            
            if prefSum[-1] == k:
                
                subArr += 1
        
        isSubArr ={}
        
        ans = 0
        
        for sum_ in prefSum:
            
            ans += isSubArr.get(sum_ - k, 0)
            
            isSubArr[sum_] = isSubArr.get(sum_, 0) + 1
            
        return ans
                