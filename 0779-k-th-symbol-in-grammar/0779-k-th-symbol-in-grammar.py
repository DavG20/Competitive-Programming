class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            
            if k == 1:
                
                return 0
            else:
                
                return 1
        else:
            
            half = 2 **(n-2)
            
            if k <= half :
                
                return self.kthGrammar(n-1 , k)
            else:
                ans = self.kthGrammar(n - 1 , k - half)
                
                if ans == 0 :
                    return 1
                else:
                    return 0