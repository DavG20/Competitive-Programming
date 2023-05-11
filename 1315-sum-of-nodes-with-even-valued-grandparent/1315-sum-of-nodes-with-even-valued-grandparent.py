# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        evenchild = []
        
        self.dfs(root , evenchild)
        
        print(evenchild)
        
        return sum(evenchild)
    
    
    def dfs(self ,root ,  evenchild ):
        
        if not root :
            
            return 
        
        if root.val % 2 == 0:
            
            if root.left :
                
                if root.left.left :
                    
                    evenchild.append(root.left.left.val)
                    
                if root.left.right :
                    
                    evenchild.append(root.left.right.val)
                
                self.dfs(root.left , evenchild)
            if root.right :
                
                if root.right.right :
                    
                    evenchild.append(root.right.right.val)
                    
                if root.right.left :
                    
                    evenchild.append(root.right.left.val)
                
                self.dfs(root.right , evenchild)
        else:
            self.dfs(root.right , evenchild)
            
            self.dfs(root.left , evenchild)
            
            
                    