# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr_node = head
        
        newHead = temp = ListNode(-101)
        
        while curr_node:
            
            if temp.val == curr_node.val:
                curr_node = curr_node.next
            else:
                temp.next = ListNode(curr_node.val)
                temp = temp.next
                curr_node = curr_node.next
                
        return newHead.next
                
                
        