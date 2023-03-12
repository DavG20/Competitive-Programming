# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        res = (self.getFreq(root , {}))
        
        
        final_dict = defaultdict(list)
        
        
        for dictt in res:
            
            final_dict[res[dictt]].append(dictt)
            
        
        final_ans = sorted(final_dict.items() , key= lambda x : x[0]  )
        
    
        
        return final_ans[-1][1]

    
        
        
        
        
    
    
    
    
    def getFreq(self ,root , ans):
        
        
        if not root :
            
            return {}
        
        
        self.getFreq(root.left , ans)
        
        ans[root.val] = ans.get(root.val , 0) + 1
        
        
        self.getFreq(root.right , ans)
        
        return ans
        
        
            
            
        
        
        