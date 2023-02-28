class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        Unique_list=[]
        max_length=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                if s[j] in Unique_list:
                    Unique_list=[]
                    break
                else:
                    Unique_list.append(s[j])
                    if max_length<j-i+1:
                        max_length=j-i+1
        return max_length
    
        
#         windows = {}
        
#         left = 0 
        
#         max_ = 0
        
#         for right in range(len(s)):
            
#             if s[right ] not in windows:
#                 windows[s[right]] = 1
#                 max_ = max(len(windows), max_)
#             else:
#                 max_ = max(max_ , len(windows))
                
#                 windows[s[left]]-= 1
                
#                 if windows[s[left]] == 0:
#                     windows.pop(s[left])
#                 left += 1
#                 print(windows)
                
#         return max_
                        
                        
                
            
            
        
        
        
        
        
        