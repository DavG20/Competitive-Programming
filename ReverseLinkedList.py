# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None 
  
class Solution(object):
    def reverseList(self,head):
        current_Node=head 
        count=0
        newHead=None 
        while current_Node:
            count+=1
            current_Node=current_Node.next 
        for i in range(count):
            newNode=ListNode(head.val)
            newNode.next=newHead
            newHead=newNode
            head=head.next 
        return newHead
      