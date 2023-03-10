# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        return self.getColRow(root , [[] , 1] , 1 ,0 , 0)
        
        
    
    
    
    
    def getColRow(self , root , ans ,max_ ,index ,  level = 0 ) :
        
        
        if not root:
            
            return [[],1]
        
        if root:
            
            if len(ans[0]) > level:
                
                ans[0][level].append(index)
                
                ans[1] = max(ans[-1] , index - ans[0][level][0] + 1)
                
                
                
            else:
                
                ans[0].append([index])
            
            # print(ans)
            
            self.getColRow(root.left , ans , max_ , 2 * (index) , level + 1)
        
            self.getColRow(root.right , ans , max_ , 2 * (index ) + 1 , level + 1)
            
        return  ans[-1]
            
            
            
            
            
        
        
        