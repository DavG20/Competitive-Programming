class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev=0
        last=1
        current=0
        if n==0 or n==1:
            return n
        for i in range (1,n):
            current=prev+last
            prev=last
            last=current
        return current
