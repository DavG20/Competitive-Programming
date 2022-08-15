# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None
class Solution(object):
    def middleNode(self,head):
        count=0
        lastNode=head
        while lastNode:
            lastNode=lastNode.next
            count+=1
        midNode=head 
        mid_index=int(count//2)
        for i in range(mid_index):
            midNode=midNode.next 
        return midNode