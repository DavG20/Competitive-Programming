# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        self.prefSum = {0 : 1}
        
        self.countPath = 0
        
        return self.traverse(root , targetSum , 0) 
        
        
    def traverse(self , root , targetSum ,total):
        
        if not root :
            return 0
        
        total += root.val
        
        
        self.countPath += self.prefSum.get(total - targetSum , 0) 
        
        self.prefSum[total] = self.prefSum.get(total , 0) + 1
        
        
        
        
        
        self.traverse(root.left , targetSum , total)
        
        self.traverse(root.right , targetSum,total)
        
        self.prefSum[total] -= 1
        
        return self.countPath
        