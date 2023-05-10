class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        
        Adj = defaultdict(list)
        
        outdegree = defaultdict(int)
        
        ans = []
        for i in range(len(graph)):
            
            outdegree[i] = len(graph[i])
            
            Adj[i] = graph[i]
            
            
        
        colors = [0] * len(graph)
        print(outdegree , Adj ) 
        for node in range(len(graph)):
            
            cycle = self.hasCycle(node , colors , Adj , ans)
            
            
            
                        
                    
         
        
        return sorted(ans)
    
    def hasCycle(self ,node , colors , adj , ans ):
        
        if colors[node] == 2:
            
            return False
        if colors[node] == 1:
            
            return True
        
        colors[node] = 1
        
        for nbr in adj[node]:
            
            cycle = self.hasCycle(nbr, colors , adj , ans)
            
            if cycle :
                return True
                
            
        
        colors[node] = 2
        
        ans.append(node)
        
        return False
        
        
            
            
            
                
     