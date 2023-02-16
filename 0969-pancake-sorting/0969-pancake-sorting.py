class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        right = len(arr)
        
        answer = []
        
        while right > 1:
            
            max_index = arr.index(right) # since they are sequential from 1 - len(arr)
            
            if max_index == right -1 :
                
                right -= 1
                
                continue
                
            if max_index != 0: #reverse the array 
                
                arr[:max_index+1] = reversed(arr[:max_index+1])
                
                answer.append(max_index+1)
            
            arr[:right] = reversed(arr[:right])
            
            answer.append(right)
            
            right -= 1
        return answer
            
            
            
            