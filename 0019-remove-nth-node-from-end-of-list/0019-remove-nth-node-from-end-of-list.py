# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size=0
        current_node=head
        while current_node:
            size+=1
            current_node=current_node.next
        count=0
        current=prev=head
    
        
        while count<size-n and current:
            count+=1
            prev=current
            current=current.next
        if current==head:
            head=head.next
        elif current is None:
            return head
        else:
            prev.next=current.next
        return head
        
            