class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        
        paths = []
        
        def dfs( arr , node):
            
            # arr.append(node)
            
            if node == target :
                
                paths.append(arr)
                
                return
            
                
                
            
            for adj in graph[node]:
                
                dfs(arr +[adj] , adj)
                
        dfs([0] , 0) 
        
        return paths
                
                