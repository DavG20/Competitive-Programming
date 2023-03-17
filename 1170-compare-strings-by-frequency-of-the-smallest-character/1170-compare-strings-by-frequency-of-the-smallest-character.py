class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        ans = [0 for _ in range(len(queries))]
        
        n = len(words)
        
        arr_word_count = []
        
        for indx , word in enumerate(words):
            count = Counter(word)
            arr_word_count.append(count[min(word)])
            
          
        arr_word_count.sort()
        
        
        arr_query_count =[]
        
        
        
        for indx, query in enumerate(queries):
            
            count = Counter(query)
            
            arr_query_count.append((count[min(query)] , indx))
            
        arr_query_count.sort()
        
        
        
        for num , indx in arr_query_count:
            
            start = 0 
            
            end = len(arr_word_count) - 1
            
            while start <= end :
                
                mid = start + (end - start) // 2
                
                if num >= arr_word_count[mid] :
                    
                    start = mid + 1
                    
                else :
                    
                    ans[indx] = n - mid
                    
                    end = mid - 1
        return (ans)
                
                    
                    
                
        
        
        
        
        
            
            
            
        