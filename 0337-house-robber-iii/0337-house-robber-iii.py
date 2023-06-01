# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dp(root ):
            
            if root is None:
                
                return (0 , 0)
            
                
            left_rob , left_not = dp(root.left )

            right_rob , right_not = dp(root.right ) 
            
            rob_curr =  left_not + right_not + root.val
            
            not_rob_curr = max(left_rob ,left_not) + max( right_rob , right_not)
            
            return (rob_curr , not_rob_curr)
            
        return max(dp(root))
            
            
            
            
            
                
        