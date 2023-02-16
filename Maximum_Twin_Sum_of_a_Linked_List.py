# class ListNode:
#     def __init__(self,val,next):
#         self.val=0
#         self.next=None 
        
class Solution(object):
    def pairSum(self,head):
        current_node=head 
        temp_result=[]
        result=[]
        while current_node:
            temp_result.append(current_node.val)
            current_node=current_node.next
        for i in range(len(temp_result)/2):
            result.append(temp_result[i]+(temp_result[len(temp_result)-1-i]))
        return max(result)
            