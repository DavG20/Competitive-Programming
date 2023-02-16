class Solution(object):
    def mostPoints(self,questions):
        length=len(questions)
        @cache
        def maxPoint(n):
            if n>=length:
                return 0
            point,brainstorm=questions[n]
            return max(point + maxPoint(n+brainstorm+1), maxPoint(n+1))
        return maxPoint(0)