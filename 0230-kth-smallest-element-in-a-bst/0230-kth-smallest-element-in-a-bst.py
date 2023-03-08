# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        return self.inOrderTrav(root)[k - 1]
        
        
    
    
    
    
    def inOrderTrav(self , root ):
        
        if root is None:
            
            return []
        
        return self.inOrderTrav(root.left) + [root.val] + self.inOrderTrav(root.right)