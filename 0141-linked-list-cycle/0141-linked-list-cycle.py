# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        fast = head 
        
        slow = head 
        
        
        while fast and fast.next:
            
            fast = fast.next.next 
            
            slow = slow.next 
            
            if fast == slow:
                return True
            
        return False
        
        
        
        
#         visited = set()
        
#         curr = head 
        
#         while curr:
#             if curr not in visited:
        
#                 visited.add(curr)
            
#             else:
                
#                 return True
#             curr = curr.next
        
#         return False
        