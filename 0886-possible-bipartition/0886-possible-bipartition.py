class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        
        visited = set([1])
        
        group = [-1 ] * (n + 1)
        
        group[0] = 1
        
        for a , b in dislikes:
            
            graph[a].append(b)
            
            graph[b].append(a)
            
        for i in range( 1 , n + 1):
            
            if group[i] == -1:
                
                if not self.dfs(graph , group , i , 0):
                    
                    return False
            
            
        return True
            
        
    def dfs(self , graph , group , vertex , color ):
        
       
        group[vertex] = color
        
        for neighbour in graph[vertex]:
        
            if group[neighbour ] == group[vertex ]:
                
                return False
            
            if group[neighbour ] ==  - 1:
                
                if not self.dfs(graph , group , neighbour ,1 - color):
                    
                    return False


                
        return True
                        
                        
                    
                
                
            
                
                
                
                
            
            
        