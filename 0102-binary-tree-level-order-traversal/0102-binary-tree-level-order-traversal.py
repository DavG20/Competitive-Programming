# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        return self.getLevelOrder(root ,[] )
        
        
        
        
        
        
    
    
    
    def getLevelOrder ( self , root , ans, level = 0 ):
        
       
        
        
        
        if root: 
            
            if len(ans) > level :
                
                ans[level].append(root.val)

            else:
                
                ans.append([root.val])
        
            self.getLevelOrder(root.left , ans ,  level + 1  )
            
            self.getLevelOrder(root.right , ans ,level + 1 )
            
            

        return ans
        
        
        
        
        
        
    
       
        
        
    
        
#     def getHeight(self , root) :
        
#         if root is None:
#             return -1
        
#         return max(self.getHeight(root.left) + 1 , self.getHeight(root.right) + 1)