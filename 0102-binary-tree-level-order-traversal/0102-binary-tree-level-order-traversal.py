# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictt=defaultdict(list)
        
        
        
        
        
        
        def help(level,root):
            if not root:
                return 
            dictt[level].append(root.val)
            
            help(level+1,root.left)
            
            help(level + 1 , root.right)
            
        help(0 , root)
        
        return dictt.values()
    
            
        
            
            
        
            
            