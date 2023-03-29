# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode] ) -> int:
        
        arr = []
        
        curr = head 
        
        max_Sum = - float('inf')
        while curr :
            
            arr.append(curr.val)
            
            curr = curr.next 
        
        n = len(arr)
        
        for i in range(n //2):
            
            max_Sum = max(max_Sum , arr[i] + arr[n - i -1])
            
        return max_Sum