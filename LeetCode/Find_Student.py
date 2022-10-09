class Solution(object):
    def chalkReplacer(self,chalk,k):
        sums=sum(chalk)
        if k>sums: #if k is greater than the sum of chalks what we care about is it's reminder
            k%=sums
        result=0
        for i in range(len(chalk)):
            k-=chalk[i]
            if k<0:
                result=i
                break
        return result
