# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current=head
        newHead=None
        newNode=temp_node=ListNode(None)
        for i in range(left-1):
            newNode.next=ListNode(current.val)
            newNode=newNode.next
            current=current.next
        for i in range(right-left+1):
            temp=ListNode(current.val)
            temp.next=newHead
            newHead=temp
            current=current.next
        while newHead:
            newNode.next=ListNode(newHead.val)
            newHead=newHead.next
            newNode=newNode.next
            
        newNode.next = current or None
        return temp_node.next
            
            
            
