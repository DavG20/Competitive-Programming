class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        # dict for number of fruit
        
        fruit_type = defaultdict(lambda : 0)
        
        
        left = 0 
        
        max_ = 0
        
        for right in range(len(fruits)):
            
            fruit_type[fruits[right]] += 1
            
            while len(fruit_type) > 2:
                
                fruit_type[fruits[left]] -= 1
                
                if fruit_type[fruits[left]] == 0:
                    fruit_type.pop(fruits[left])
                
                left += 1
            max_ = max(max_ , sum(fruit_type.values()))
            
        return max_
            
                
            