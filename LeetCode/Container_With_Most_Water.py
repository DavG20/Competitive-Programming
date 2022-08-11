class Solution(object):
    def maxArea(self,height):
        output=0
        for i in range(len(height)):
            j=i+1
            for j in range(len(height)):
                temp=min(height[i],height[j])
                if temp*(j-i)<output:
                    j+=1
                else:
                    output=temp*(j-i)
                    j+=1
        return(output)
c=Solution()
c.maxArea([1,8,6,2,5,4,8,3,7])