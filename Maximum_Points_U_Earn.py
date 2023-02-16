class Solution(object):
    def maxScore(self,cardPoints,k):
        best=total=sum(cardPoints[:k])
        print(best)
        for i in range(k-1,-1,-1):
            total +=cardPoints[i+len(cardPoints)-k]-cardPoints[i] #subtract from the end to compare
        best=max(best, total)
        return best
