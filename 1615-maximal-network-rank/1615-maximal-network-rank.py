class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        
        
        if len(roads) == 0:
            return 0
        
        adj_list = defaultdict(list)
        
        
       
        pair = []
        
        
        for a , b in roads:
                       
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        for val , adj in adj_list.items():
            pair.append((val , len(adj)))
            
        pair.sort(key = lambda x : x[1])
        
        max_ = 0
        
        
        check = set ((a,b) for a, b in roads)
        
        
        for i in range(len(pair)):
            a , adj_A = pair[i]
            
            for j in range(len(pair)):
                
                if i != j:
                    
                    b , adj_B = pair[j]
                    
                    
                    if (a, b) not  in check and (b,a) not  in check:

                        max_ = max(max_, adj_A + adj_B )
                    else:
                        max_ = max(max_, adj_A + adj_B - 1)
                        
        
        return max_
        
        
        