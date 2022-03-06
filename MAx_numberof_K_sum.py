from collections import defaultdict


class Solution(object):
    def maxOperations(self, nums, k):
        hash = defaultdict(int)
        count = 0 
        for num in nums:
            target = k - num
            print(hash[target])
            if hash[target] > 0:
                hash[target] -= 1
                count += 1
            else:
                hash[num] += 1
                
        return count 
        
c=Solution()
print(c.maxOperations([1,2,3,4],
5))
