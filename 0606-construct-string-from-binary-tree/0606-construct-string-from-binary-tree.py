# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = []
        
        self.getStr(root, res)
        
        return "".join(res)
        
        
        
        
    def getStr(self ,root , result):
        
        if root is None:
            return 
        
        result.append(str(root.val))
        
        
        
        if not root.left and not root.right :
            return 
        
        
        result.append("(")
        
        self.getStr(root.left , result)  
        
        result.append(")"  )
        
        if root.right is not None:
            result.append("(")
            self.getStr(root.right , result) 
            result.append(")"  )
        