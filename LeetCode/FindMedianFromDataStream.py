import heapq
class MedianFinder:
    def __init__(self):
        self.left_part=[]
        self.right_part=[]
    def addNum(self,num:int)->int:
        heapq.heappush(self.left_part, -heapq.heappushpop(self.right_part, num))
        if len(self.left_part)>len(self.right_part):
            heapq.heappush(self.right_part, -heapq.heappop(self.left_part))
    def findMedian(self)->float:
        if len(self.left_part)<len(self.right_part):
            return float(self.right_part[0])
        else:
            return (-self.left_part+self.right_part)/2.0
    
