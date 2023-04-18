"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        ans = []
        
        if root is None: 
            
            return 0
        

        max_ = 0
        
        for child in root.children:
            
            max_ = max(max_ , self.maxDepth(child))
            
         
        return max_ + 1
   