class Solution:
    def fib(self, n: int ) -> int:
        memo = defaultdict(int)
        def fibb(n):
            if n == 0 :

                return 0 

            if n == 1 :

                return 1 
            memo[n] = fibb(n - 1) + fibb(n - 2)



            return memo[n]
        
        return fibb(n)
        