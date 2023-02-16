class Solution(object):
    def isPowerOfThree(self,n):
        count=0
        if(n==1):
           return True
        else:
            while n%3==0 and n//3>=1:
                count+=1
                n=n//3    
        if n==1 and count>=1:
            return True
        else:
            return False
c=Solution()
print(c.isPowerOfThree(3))