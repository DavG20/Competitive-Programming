import heapq

class Solution:
    def kthSmallest(self,matrix,k):
        heap=[]
        for i in range(len(matrix)):
            heap+=matrix[i]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        