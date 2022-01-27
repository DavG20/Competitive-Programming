class Solution:
    def kClosest(self, points,k):
        points.sort(key=self.distance)
        return points[:k]
    
    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2
x=Solution()
print(x.kClosest([[0, 2], [-3, 3], [-2, 5], [6, 10]],3))