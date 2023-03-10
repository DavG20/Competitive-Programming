# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        return self.getAvg(root)[-1]
        
        
        
        
    def getAvg(self, root ):
        
        
        if not root :
            
            return [0 ,0 ,0]
        
        
        leftArr =  self.getAvg(root.left)
        
        rightArr = self.getAvg(root.right )
        
        totalSum = leftArr[0] + rightArr[0] + root.val 
        
        
        totalNumNode = leftArr[1] + rightArr[1] + 1
        
        
        count = leftArr[2] + rightArr[2] 
        
        
        if totalSum // totalNumNode == root.val:
            
            count += 1
            
        return [totalSum,totalNumNode, count]
        
        
        
        
        
        
        
        