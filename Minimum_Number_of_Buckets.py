class Solution(object):
    def minimumBuckets(self,street):
        Hb=list(street)
        n=len(Hb)
        for i,char in enumerate(Hb):
            if char=="H":
                if i>0 and Hb[i-1]=="B":
                    continue
                if i+1<n and Hb[i+1]==".":
                    Hb[i+1]="B"
                elif i>0 and Hb[i-1]==".":
                    Hb[i-1]="B"
                else:
                    return -1 
        return Hb.count('B')
