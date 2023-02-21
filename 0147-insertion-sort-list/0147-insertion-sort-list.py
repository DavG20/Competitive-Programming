# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        
        newNode = ListNode(-5001)
        
        while curr:
            
            prev_node = newNode
            
            while prev_node.next and prev_node.next.val < curr.val:
                prev_node = prev_node.next
            
            nextNode = curr.next 
            
            curr.next = prev_node.next 
            
            prev_node.next = curr
            
            curr = nextNode
            
        return newNode.next
            
       
        
        