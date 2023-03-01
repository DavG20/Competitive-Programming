# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        arr = []
        
       
        curr = head 
        
        stack = []
    
        
        index = 0
        
        while curr:
            
            # add the default values
            
            arr.append(0)
            
            
            
            while stack and curr.val > stack[-1][1]:
                
                arr[stack.pop()[0]] = curr.val 
            
            stack.append((index,curr.val))
            
            
            index += 1 
            curr = curr.next
        
        return(arr)
        
        
        
        
        
        
        
        