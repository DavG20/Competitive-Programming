class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(n , memo):
            if n == 0:

                return 0

            if n == 1 :

                return 1

            if n == 2 :

                return 1

            if n not in memo:
                memo[n] = dp(n - 3 , memo ) +  dp(n - 2 ,memo ) +  dp(n - 1  , memo)

            return memo[n]
        
        return dp(n , defaultdict(int))
        
        
        
        