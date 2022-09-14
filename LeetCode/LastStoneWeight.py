import heapq
class Solution:
    def lastStoneWeight(self,stones):
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>=2:
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap, (x-y))
        return -heap[-1] if heap else 0
c=Solution()
print(c.lastStoneWeight([1]))