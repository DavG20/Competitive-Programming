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
            
            root.right = self.deleteNode(root.right ,key)
            
        elif root.val > key :
            
            root.left =  self.deleteNode( root.left , key)
            
        else:
            
            if  root.left == None:
                
                return root.right
            
            if not root.right :
                
                return root.left
            
            newNode = self.inOrderTra(root.right)
            
            
            # swap the value
            
            
            root.val = newNode.val 
            
            root.right =  self.deleteNode(root.right , newNode.val )
            
        return root
            
            
        
        
        
        
        
        
    
    
    
    
    
    def inOrderTra(self, root):
        
            curr = root 
            
            
            while curr.left :
                
                curr = curr.left 
            return curr
        
        
        
        
    
    
    
    
    
        
        