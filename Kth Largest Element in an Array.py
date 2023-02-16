import heapq
class Solution:
    def findKthLargest(self,nums):
        # nums.sort()
        # return nums[len(nums)-k] # we can do in this way 
                #OR
        heap=[]
        for num in nums:
            heapq.heappush(heap,-num)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)