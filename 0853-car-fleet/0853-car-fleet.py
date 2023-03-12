class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # lets get destination time using  position and speed together
        
        
        stack = []
        
        
        count = 0
        
        
        for i , pos in enumerate(position):
            
            position[i]=(pos,(target - pos) / speed[i])
        
        
        position.sort(key = lambda x:x[0]  , reverse = True)
        
        
        
        for arriv in position:
            
            
            while stack and stack[-1] < arriv[1]:
                
                stack.pop()
                
            if stack and stack[-1] >= arriv[1]:
                
                count += 1
            
            
            stack.append(arriv[1])
            
        return len(position ) - count
                
                
            
            
            
        
        
        
        
        
        
        
        #sort the cars based on their pos 
        
        
        
        
        
        
        
        
        
        
        
        
        