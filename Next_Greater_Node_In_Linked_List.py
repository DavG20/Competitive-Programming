# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None
class Solution(object):
    def nextLargerNodes(self,head):
        prev_Node=head
        next_Node=ListNode(0)
        next_Node.next=head
        result=[]
        if head==None:
            return []
        while prev_Node :
            while next_Node.next and next_Node.next.val<=prev_Node.val:
                next_Node=next_Node.next 
            if next_Node.next==None:
                next=prev_Node.next 
                result.append(0)
                next_Node=next
                prev_Node=prev_Node.next
                
            else:
                next=prev_Node.next 
                result.append(next_Node.next.val)
                next_Node=next
                prev_Node=prev_Node.next
                print(newNode)
        return result
            
            
            
            