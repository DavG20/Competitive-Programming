class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        num_Com = 0
        
        n = len(isConnected)
        
        visited = [False for _ in range(n)]
        
        for i in range(n):
            if not visited[i]:
                num_Com += 1
                self.dfs(i , isConnected , visited)
                
        return num_Com
            
        
    
    
    def dfs(self, node, isConnected , visited ):
        
        
        visited[node] = True
        
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visited[i]:
                self.dfs(i , isConnected , visited)
            