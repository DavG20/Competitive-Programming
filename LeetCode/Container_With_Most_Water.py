class Solution(object):
    def maxArea(self,height):
        left,right=0,len(height)-1
        result=0
        while left<right:
            water=(right-left)*min(height[left],height[right])
            if water>result:
                result=water
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return result
c=Solution()
print(c.maxArea([1,8,6,2,5,4,8,3,7]))