class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefSum = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefSum[i + 1][j + 1] = self.prefSum[i][j + 1] + self.prefSum[i + 1][j] - self.prefSum[i][j] + matrix[i][j]
        
        # print(self.prefSum)
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.prefSum[row2 + 1][col2 + 1] - self.prefSum[row2 + 1][col1] - self.prefSum[row1][col2 + 1] + self.prefSum[row1][col1]

["NumMatrix","sumRegion"]
[[[[2,1,3],[0,4,5],[1,3,6]]],[1,1,2,2]]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)