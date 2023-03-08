# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        arr = self.getCordinate(root , [], 0 , 0)
        
        
        
        arr.sort()
        

        
        result = defaultdict(list)
        
        for tup , val in arr:
            
            result[tup[0]].append(val)
            
        
        
        ans = []
        
        for dic in result:
            
            ans.append(result[dic])
            
        return ans
        
        
        
    
    
    def getCordinate(self, root , arr , row , col ):
        
        if root :
            
            arr.append(((col , row) ,root.val))
            
            self.getCordinate(root.left ,  arr ,row + 1 , col - 1)
            
            self.getCordinate(root.right  , arr , row + 1 , col + 1)
        return arr
            
            
            
            
        
        
    
    
    
    
        
        
        