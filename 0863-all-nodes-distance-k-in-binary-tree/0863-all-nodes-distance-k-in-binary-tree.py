# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        self.travers(root, graph)
        # print(graph[target.val])
        queue = deque(graph[target.val])
        print(queue)
        visited = set([target.val])
        ans = []
        count = k 
        if k == 0:
            return [target.val]
        while queue :
            
            level = len(queue)
            count -= 1
            
            for i in range(level):
                node = queue.popleft()
                
                visited.add(node)
                
                if count == 0:
                    ans.append(node)
                
                for nbr in graph[node]:
                    if not nbr in visited:
                        visited.add(nbr)
                        queue.append(nbr)
                    # if count == 0:
                    #     ans.append(nbr)
                        
        return ans
                
    
    
    
    def travers(self , root , graph):
        
        if  not root:
            
            return 
        
        
        if root.left :
            graph[root.val].append(self.travers(root.left , graph))
            graph[root.left.val].append(root.val)
        
        if root.right :
            graph[root.val].append(self.travers(root.right , graph))
            graph[root.right.val].append(root.val)       
        
        return root.val
        