from this import d


class Solution(object):
    def maxCoins(self,piles):
        piles.sort()
        count=int(len(piles))
        coin=0
        while count>0:
            data=piles[-3:]
            coin+=data[1]
            piles.pop()
            piles.pop()
            piles.pop()
            print(data, data[1])
            print(count)
            count-=3
        return coin