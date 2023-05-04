# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
                
        if not root :
            
            return 
        
        ans = []
        
        self.dfs(root , "" , ans)
        print(ans)
        
        return sum(ans)
        
    def dfs(self , root , total , ans):


        if root:
            total += str(root.val)
           
            self.dfs(root.left , total , ans )



            self.dfs(root.right  ,total , ans )

            if root.left is None and root.right is None:
                
                ans.append(int(total))
                
                

        return 


    

        
        
        
            
            