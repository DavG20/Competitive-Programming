class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        if rowIndex == 0:
            return [1]
        
        elif rowIndex == 1:
            return [1,1]
        
        else:
            Row = [1]
            
            lastRow = self.getRow(rowIndex - 1)
            
            for i in range(len(lastRow) - 1):
                
                Row.append(lastRow[i] + lastRow[i + 1])
                
            Row.append(1)
            
            return Row
        return self.getRow(rowIndex)
                
            