# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        if not root :
            
            return root
        
        if root.val < key :
            
            root.right = self.deleteNode(root.right  , key)
            
        elif root.val > key :
            
            root.left  = self.deleteNode( root.left  , key)
            
        else:
            
            if not root.left :
                
                return  root.right 
            
            if not root.right  :
                
                return root.left 
            
            #let find inorder successor
            
            inorderSucc = self.findInorderSucc(root.right)
            
            
            #swap the value of root and inorder succ 
            
            
            root.val = inorderSucc.val 
            
            
            root.right  =  self.deleteNode(root.right , inorderSucc.val)
        
        return root
    
    
    def findInorderSucc(self , node):
        
        curr = node 
        
        while curr.left :
            
            curr = curr.left 
            
        return curr
            
            
            
        
        
        
        
        