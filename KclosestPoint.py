class Solution:
    def kClosest(self, points,k):
        points.sort(key=self.squared_distance)
        return points[:k]
    
    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2