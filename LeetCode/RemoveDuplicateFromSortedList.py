# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=0
#         self.next=None
class Solution(object):
    def deleteDuplicates(self,head):
        if head:
            prev_head,current_head=head,head.next 
            while prev_head and current_head:
                if prev_head.val==current_head.val:
                    prev_head.next=current_head.next 
                else:
                    prev_head=prev_head.next 
                current_head=current_head.next
        return head