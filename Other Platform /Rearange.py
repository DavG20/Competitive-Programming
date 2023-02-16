def rearrangeArray(nums):
    for i in range(len(nums)-2):
        if(nums[i+1]==(nums[i]+nums[i+2])/2):
            nums[i+1],nums[i+2]=nums[i+2],nums[i+1]
    return nums
