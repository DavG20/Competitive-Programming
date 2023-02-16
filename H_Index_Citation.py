class Solution(object):
    def hIndex(self,citations):
        h=0
        length=len(citations)
        for index ,value in enumerate(sorted(citations)):
            h=max(h,min(length-index,value))
        return h
