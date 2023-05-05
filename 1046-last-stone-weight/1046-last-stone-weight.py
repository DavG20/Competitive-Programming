class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        arr = [-stone for stone in stones ]
                
        heap = list(arr)
        heapq.heapify(heap)
        
        diff = 0 
        while len(heap) > 1:
            
                
            v1 = heapq.heappop(heap)
            heapify(arr)
            v2 = heapq.heappop(heap)

            if v1 != v2 :

                diff = v1 - v2

                if diff != 0 :

                    heap.append(diff)
                    heapq.heapify(heap)
           
                
                
                    
        print(heap)             
         
            
        
        return -sum(heap)