# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None 
class Solution(object):
    def removeNthFromEnd(self,head,n):
        Current_Node=store_Node=head
        count=0
        while Current_Node:
            Current_Node=Current_Node.next 
            count+=1 
        if count==n:
            head=head.next
            return head
        for i in range(1,count-n):
            head=head.next
        if head :
            head.next=head.next.next
        return store_Node
            