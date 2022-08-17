# class ListNode:
#     def __init__(self,val,next):
#         self.val=0
#         self.next=None
class Solution(object):
    def isPalindrome(self,head):
        result=[]
        current_node=head 
        while current_node:
            result.append(current_node.val)
            current_node=current_node.next 
        return result==result[::-1]