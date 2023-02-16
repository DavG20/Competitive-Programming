class Solution:
    def PredictTheWinner(self, nums):
        if len(nums)%2==0:
            return True
        scores=[0,0]
        for index in range((len(nums))):
            if index%2==0:
                scores[0]+=nums[index]
            else:
                score[1]+=nums[index]
        odd,even=scores
        
        PlayerOneFirstMove=max(nums[0],nums[-1])
        PlayerTwoChoice=max(odd-PlayerOneFirstMove,even)
        PlayerOneFinalChoose=min(odd-PlayerOneFirstMove,even)
        if PlayerTwoChoice<=PlayerOneFirstMove+PlayerOneFinalChoose:
            return True
        else:
            return False