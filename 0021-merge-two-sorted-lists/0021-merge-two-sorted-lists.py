# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        list1_node = list1 
        
        list2_node = list2 
        
        mergeNode = dummy = ListNode(None)
        
        while list1_node and list2_node:
            
            if list1_node.val <= list2_node.val:
                dummy.next = ListNode(list1_node.val)
                
                dummy = dummy.next 
                
                list1_node = list1_node.next
                
            else:
                
                dummy .next = ListNode(list2_node.val)
                
                dummy = dummy.next 
                
                list2_node = list2_node.next 
                
        while list1_node:
            dummy.next = ListNode(list1_node.val)
                
            dummy = dummy.next 
                
            list1_node = list1_node.next
            
        while list2_node:
            dummy .next = ListNode(list2_node.val)

            dummy = dummy.next 

            list2_node = list2_node.next 
            
        return mergeNode.next

            
            
            