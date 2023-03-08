# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        return self.getRightSideElm(root , [], 0)

    
    
    def getRightSideElm(self , root , ans , level = 0):
        
        if root :
            
            if len(ans) == level :
                
                ans.append(root.val )
            
            self.getRightSideElm(root.right , ans , level + 1)
            
            self .getRightSideElm(root.left , ans , level + 1)
            
            
        return ans
        
        
        
            
        
        