# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        
        
        while curr:
            
            temp = head 
            
            
            while temp != curr:
                
                #swap if val is not in the right place
                if temp.val > curr.val:
                    
                    temp.val , curr.val = curr.val , temp.val
                    
                temp = temp.next 
            curr = curr.next 
        return head
                
          
                
            
            
        
        