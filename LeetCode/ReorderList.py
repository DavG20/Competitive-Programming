# class ListNode:
#     def __init__(self,val,next):
#         self.val=val
#         self.next=None 
        
class Solution(object):
    def reorderList(self,head):
        count_node=head
        current_node=head 
        newNode=ListNode(0)
        result=[]
        i=0
        while count_node:
            result.append(count_node.val)
            count_node=count_node.next 
        if len(result)%2==0:
            while i<len(result)/2:
                next_node=current_node.next
                newNode.next=current_node
                newNode.next.next=ListNode(result[len(result)-1-i])
                newNode=newNode.next.next 
                current_node=next_node
                i+=1
        else:
            while i<len(result)/2:
                next_node=current_node.next 
                newNode.next=current_node
                newNode.next.next=ListNode(result[len(result)-1-i])
                newNode=newNode.next.next 
                current_node=next_node
                i+=1
            newNode.next=ListNode(result[int(len(result)//2)])
        return newNode.next