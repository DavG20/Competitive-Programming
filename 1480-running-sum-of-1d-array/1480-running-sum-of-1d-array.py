class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
            
        
#         arr = []
        
#         for num in nums:
#             if arr != []:
#                 arr.append(arr[-1] + num)
#             else:
#                 arr.append(num)
#         return arr
        
        