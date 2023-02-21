# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return head 
        
        size = 1 
        
        curr_node = head 
        
        
        while curr_node.next :
            
            size += 1
            
            curr_node = curr_node.next 
        
        #make the cycle here
        
        curr_node.next = head 
        
        shift = size - (k % size)
        
        while shift:
            
            shift -= 1
            
            curr_node = curr_node.next 
            
        newHead = curr_node.next 
        
        curr_node.next = None
        
        return newHead
        