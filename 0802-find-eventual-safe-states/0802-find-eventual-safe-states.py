class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        outDegree = defaultdict(int)
        
        Adj = defaultdict(list)
        
        for i in range(len(graph)):
            
            outDegree[i] = len(graph[i])
            
            Adj[i] = graph[i]
            
        ans = []
        
        colors = [0] * len(graph)
        
        for node in range(len(graph)):
            
            self.hasCycle(node , Adj , ans , colors)
            
        return sorted(ans)
            
    def hasCycle(self, node , Adj , ans , colors):
        
        if colors[node] == 2:
            
            return False
        #has cycle because it goes to the currnet processing node
        if colors[node] == 1:
            
            return True
        
        #change the node color to processing state
        
        colors[node] = 1
        
        for nbr in Adj[node]:
            
            hasCycle = self.hasCycle(nbr , Adj , ans , colors)
            
            # becase the nbr is note a terminal or a safe node so before appending just return true
            if hasCycle :
                
                return True
        
        colors[node] = 2
        
        ans.append(node)
        
        return False
            
        
            
            
            
            
            
            
            
        