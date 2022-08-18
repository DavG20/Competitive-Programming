# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=0
#         self.next=None
class Solution(object):
    def deleteDuplicates(self,head):
        newNode=ListNode(0)
        newNode.next=head 
        fast,slow=head,newNode
        if head==None:
            return head
        while fast:
            while fast.next and fast.val==fast.next.val:
                fast=fast.next 
            if slow.next==fast:
                slow,fast=slow.next,fast.next
            else:
                slow.next=fast.next
                fast=slow.next 
        return newNode.next