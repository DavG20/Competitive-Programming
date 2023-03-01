class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        
        array = [0 for _ in range(len(s))]
        
        
        for start , end , dirc in shifts:
            
            if dirc:
                array [start] += 1
            
                if end + 1 < len(s):

                    array[end + 1] -= 1
            else:
                array[start] -= 1
                
                if end + 1 < len(s):
                    
                    array[end + 1] += 1
        for i in range(1,len(array)):
            
            array[i] = array[i] + array[ i - 1 ]
            
        
        ans = ""
        
        for i in range(len(s)):
            
            ans += str(chr(((ord(s[i]) + array[i] - 97) % 26) + 97))
            
        return ans
        
        
            
            
                
        