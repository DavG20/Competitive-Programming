# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val 
#         self.next=None 
        
class Solution(object):
    def reverseKGroup(self,head,k):
        if head==None:
            return head
        if k<2:
            return head 
        prev_node,next_node=None,None 
        current_node=head 
        size=0
        count=0
        count_node=head
        while count_node:
            size+=1
            count_node=count_node.next
        while current_node and count<k and size-k>=0:
            next_node=current_node.next 
            current_node.next=prev_node 
            prev_node=current_node 
            current_node=next_node 
            count+=1
        size=size-count 
        if next_node and size-k>=0:
            head.next=self.reverseKGroup(next_node, k)
        else:
            head.next=current_node
        return prev_node