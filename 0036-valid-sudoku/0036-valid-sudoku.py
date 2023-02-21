class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [ set() for _ in range(9)]
        
        cols = [set() for _ in range(9)]
        
        
        sub_box = [[set() for _ in range(3)] for _ in range(3)]
        
        
        for i in range(9):
            
            for j in range(9):
                
                curr_cell =  board[i][j]
                
                if curr_cell == ".":
                    continue
                
                elif (curr_cell in rows[i]) or (curr_cell in cols[j]) or (curr_cell in sub_box[i//3][j//3]):
                    return False
                
                
                rows[i].add(curr_cell)
                
                cols [j].add(curr_cell)
                
                sub_box[i//3][j//3].add(curr_cell)
                
        return True
                
            
            
        
        
        