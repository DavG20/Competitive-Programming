# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        fast = head 
        
        slow = head 
        
        while fast and fast.next:
            
            fast = fast.next.next 
            
            slow = slow.next 
            
            if slow == fast:
                fast = head 
                break
                
         
        
        while fast and fast.next:
                        
            if slow == fast:
                return slow 
            fast = fast.next 

            slow = slow.next 
        
                    
                    
        
        
        
        
#         visited = set()
        
#         curr_node = head 
        
        
#         while curr_node:

#             if curr_node not in visited:

#                 visited.add(curr_node)
#             else:
#                 return curr_node
            
#             curr_node = curr_node.next
            
#         return None

        
        