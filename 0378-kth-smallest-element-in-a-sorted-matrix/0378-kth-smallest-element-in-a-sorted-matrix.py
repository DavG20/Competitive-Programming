class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        
        heapq.heapify(arr)
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                heapq.heappush(arr,-matrix[i][j])
                
                while len(arr) > k:
                    
                    heapq.heappop(arr)
                    
        print(arr)
        
        return -arr[0]
        