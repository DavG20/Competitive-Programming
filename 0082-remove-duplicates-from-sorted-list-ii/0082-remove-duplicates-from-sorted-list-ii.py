# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode(None)
        newHead.next = head
        slow = newHead 
        
        fast = head
        
        while fast :
            
            while fast.next and fast.val == fast.next.val:
                fast = fast.next 
                
            if slow.next == fast:
                
                slow = slow.next 
                
                fast = fast.next 
                
            else:
                
                slow.next = fast.next 
                
                fast = fast.next 
        return newHead.next
                
                
        