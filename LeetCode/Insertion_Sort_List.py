# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.next=None 
#         self.val=val 

class Solution(object):
    def insertionSortList(self,head):
        newNode=ListNode(0)
        current_node=head 
        if head==None and head.next==None:
            return head 
        while current_node:
            prev_node=newNode
            while prev_node.next and prev_node.next.val<current_node.val:
                prev_node=prev_node.next 
            next_node=current_node.next 
            current_node.next=prev_node.next 
            prev_node.next=current_node
            current_node=next_node
        return newNode.next        
        