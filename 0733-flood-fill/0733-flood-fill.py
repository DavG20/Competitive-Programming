class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        
        
        originColor = image[sr][sc]
        
        if originColor == color: return image 
        
        
        self.dfs(sr , sc , image , originColor , color)
        
        return image
        
    def dfs(self , sr , sc , image , originColor , color):

        n = len(image)

        m = len(image[0])

        if image[sr][sc] == originColor:

            image[sr][sc] = color 

            if sr + 1 < n :
                self.dfs(sr + 1 , sc , image , originColor, color)
            if sr - 1 >= 0 :
                self.dfs(sr - 1 , sc , image , originColor, color)
            if sc + 1 < m :
                self.dfs(sr  , sc + 1 , image , originColor, color)
            if sc - 1 >= 0 : 
                self.dfs(sr  , sc - 1 , image , originColor , color)
                    