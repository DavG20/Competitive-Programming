class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        
        dict_greater = {}
        
        
        answer = []
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                
                if stack[-1] < num:
                    
                    dict_greater [stack[-1]] = num
                    
                    stack.pop()
        
                
                
            stack.append(num)
            
        for num in nums1:
            
            if num in dict_greater:
                
                answer.append(dict_greater[num])
            else:
                
                answer.append(-1)
        return answer
                
            
                
            