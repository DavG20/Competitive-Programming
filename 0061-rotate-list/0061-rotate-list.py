# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        size = 1
        
        curr = head 
        
        while curr.next:
            
            size += 1
            
            curr = curr.next 
        
        curr.next = head
        
        shift = size - ( k % size ) 
        
        
        
        while shift > 0 :
            
            curr = curr.next 
            
            shift -= 1
        
        newHead = curr.next
        
        # cut the cycle
        
        curr.next = None
        
        
        return newHead
        
    
        
        
            
        