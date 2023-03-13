# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        return self.MergeSort(head)     
        
        
    
    
    def Merge(self , root1 , root2):
        
        
        dummy = ListNode(0)
        
        Merged_Node = dummy
        
        
        while root1 and root2 :
            
            if root1.val <= root2.val:
                
                Merged_Node.next = root1
                
                root1 = root1.next 
                
                
            else:
                
                Merged_Node.next = root2
                
                root2 = root2.next 
                
            Merged_Node = Merged_Node.next 
        
        
        if root1:
            
            Merged_Node.next = root1
            
        if root2 :
            
            Merged_Node.next = root2
            
        return dummy.next 
            
            
                
                
    def MergeSort(self , root):
        
        
        if not root or not root.next :
            
            return  root
        
        middle_node = self.getMid(root)
        
        
        right = self.MergeSort(middle_node.next)
        
        middle_node.next = None
        
        left = self.MergeSort(root)
        
        return self.Merge(left , right)
        
        
        
        
        
        
    def getMid(self,root):
        
        if not root or not root.next :
            return None
        
        slow = root 
        
        fast = root.next 
        
        while fast.next and fast.next.next:
            
            slow = slow.next 
            
            fast = fast.next.next
            
        return slow
    
    
    
    
        
        
        
        
        