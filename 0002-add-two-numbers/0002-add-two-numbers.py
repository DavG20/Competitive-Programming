# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        node1 = l1
        
        node2 = l2
        
        
        num1 = ""
        
        while node1:
            num1 += str(node1.val)
            
            node1 = node1.next 
        
        num2 = ""
        
        while node2:
            num2 += str(node2.val)
            
            node2 = node2.next 
            
        res = str( int(num1[::-1]) + int(num2[::-1]))[::-1]
        
        newNode = temp = ListNode(None)
        
        for char in res:
            
            temp.next = ListNode(int(char))
            
            temp = temp.next 
            
        return newNode.next 
    
            
            
                  
                  
        
        
            
        