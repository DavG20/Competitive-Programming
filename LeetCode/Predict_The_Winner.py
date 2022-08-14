class Solution:
    def PredictTheWinner(self, nums):
        if len(nums) % 2 == 0:
            return True
        
        else:
            scores = [0,0]
            for idx in range(len(nums)):
                if idx % 2 ==0: #because of 0 indexed array even in the array is odd actually
                    
                    scores[0] += nums[idx]
                else:
                    scores[1] += nums[idx]
                        
            odd, even = scores
            minimalSum = min(odd, even)
            
            player1FirstMove = max(nums[0],nums[-1])
            oddAfterMove1 = odd - player1FirstMove
            player2ChoiceForGame = max( oddAfterMove1, even )
            player1ChoiceForGame = min( oddAfterMove1, even )

            if player2ChoiceForGame <= player1ChoiceForGame + player1FirstMove:
                return True
            else:
                return False
            
            
