class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)      
        
        val_key = []
        
        
        for key , val in count.items():
            
            val_key.append((-val , key))
        
        val_key.sort()
        
        heapq.heapify(val_key)
        
        ans = []
        
        for i in range(k):
            
            ans.append(heapq.heappop(val_key)[1])
            
        print(ans)    
        return ans
        
        
        
        
        
        