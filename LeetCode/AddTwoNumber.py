class Solution(object):
    def addTwoNumber(self,l1,l2):
        num_one=""
        num_two=""
        while l1:
            num_one=str(l1.val)+num_one
            l1=l1.next
        while l2:
            num_two=str(l2.val)+num_two
            l2=l2.next
        final_Num=int(num_one)+int(num_two)
        newHead=None
        i=0
        while i<len(final_Num):
            newNode=ListNode(final_Num[i])
            newNode.next =newHead
            newHead=newNode
            i+=1
        return newHead
c=Solution()
c.addTwoNumber([2,4,3], [5,6,4])