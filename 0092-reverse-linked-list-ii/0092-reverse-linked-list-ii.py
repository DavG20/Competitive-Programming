# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        array = []
        
        currNode = head
        
        while currNode :
            
            array.append(currNode.val)
            
            currNode = currNode.next 
        
    
        array[:] = array[:left-1] + array[left-1:right][::-1] + array[right:]
            
        newNode = answerNode = ListNode(None)
        
        
        for num in array:
            
            newNode.next = ListNode(num)
            
            newNode = newNode.next
            
        return answerNode.next
        