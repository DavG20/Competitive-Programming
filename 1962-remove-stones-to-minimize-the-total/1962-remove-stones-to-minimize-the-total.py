class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            
            piles[i] = - piles[i]
            
        heapq.heapify(piles)
        
        print(piles)
        
        for i in range(k):
            
            big_val = heapq.heappop(piles)
            
            val = big_val + (-big_val //2)
            
            heapq.heappush(piles , val)
            
            # heapq.heapify(piles)
            
        return -sum(piles)
        
        
        
        
        
        
        