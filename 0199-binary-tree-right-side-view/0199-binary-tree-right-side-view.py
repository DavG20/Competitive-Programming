# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        dictt = defaultdict(list)
        
        return self.getRightSideView(root , dictt , 0)
    
    
    def getRightSideView(self , root , dictt , level = 0 ):
        
        
        if root :
            
            dictt[level] = root.val 
            
            self.getRightSideView(root.left , dictt , level + 1)
            
            self.getRightSideView(root.right , dictt, level + 1)
            
        return dictt.values()