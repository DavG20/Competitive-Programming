# class ListNode:
#     def __init__(self,val,next):
#         self.val=val
#         self.next=None 
class Solution(object):
    def deleteMiddle(self,head):
        counter_node=head 
        prev_node=currnet_node=head 
        size=0
        i=0
        if not head or not head.next:
            return None 
        while counter_node:
            size+=1
            counter_node=counter_node.next 
        if size%2==0:
            mid=size/2
            while currnet_node.next and i<mid:
                prev_node=currnet_node
                currnet_node=currnet_node.next
                i+=1
            prev_node.next=currnet_node.next 
        else:
            mid=(size-1)/2
            while currnet_node.next and i<mid:
                prev_node=currnet_node
                currnet_node=currnet_node.next 
                i+=1
            prev_node.next=currnet_node.next
        return head