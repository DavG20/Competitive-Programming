# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None
class Solution(object):
    def swapPairs(self,head):
        newNode=ListNode(0)
        newNode.next=head 
        result_node=newNode
        while newNode.next and newNode.next.next:
            first_node=newNode.next
            second_node=newNode.next.next
            first_node.next=second_node.next 
            second_node.next=first_node
            newNode.next=second_node
            newNode=newNode.next.next 
        return result_node.next
            