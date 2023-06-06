class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
        def dp(pos , questions , memo):
            
            if pos >= len(questions):
                return 0
            if not pos in memo: 
                solve = dp(pos + questions[pos][1] + 1 , questions , memo) + questions[pos][0]

                skip = dp(pos + 1 , questions , memo)

                memo[pos] =max(solve , skip)
                
            return memo[pos]
        
        memo = defaultdict(int)
        
        return dp(0 , questions,memo)