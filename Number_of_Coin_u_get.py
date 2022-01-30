class Solution(object):
    def maxCoins(self,piles):
        piles.sort()
        count=int(len(piles))
        coin=0
        while count>0:
            data=piles[-2:]
            coin+=data[0]
            piles.pop()
            piles.pop()
            piles.remove(min(piles))
            print(data, data[1])
            print(count)
            count-=3
        print(coin)
        return coin
c=Solution()
c.maxCoins([1,2,3,4,5,6,7,8,9])