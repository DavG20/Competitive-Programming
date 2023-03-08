# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], max_ =  float('inf'), min_ = - float('inf')) -> bool:
        
        
        
        
        if root is None:
            
            return True
        
        
        if root.val <= min_ or root.val >= max_ :
            
            return False
        
        return self.isValidBST(root.left ,min(max_ , root.val) , min_) and self.isValidBST(root.right ,max_ , max(min_ , root.val))
        
        
       
        
        
        
        