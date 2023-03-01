# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        fast = head
        
        slow = head 
        
        while fast and fast.next:
            
            slow = slow.next 
            
            fast = fast.next.next
            
        return slow
        
        
#         curr = head 
        
#         arr  = []
        
#         while curr:
#             arr.append(curr)
#             curr = curr.next 
#         return arr[len(arr)//2]
            
        
        
        
#         size = 0
        
#         curr_node = head 
        
#         while curr_node :
            
#             size += 1
            
#             curr_node = curr_node.next 
            
#         mid = size // 2
        
#         curr = head 
#         while mid:
            
#             curr = curr.next 
#             mid -= 1
#         return curr
            
    
        