class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dict_ing = defaultdict(list)
        
        indegree = {recipes[i]:0 for i in range(len(recipes))}
        
        for i in range(len(recipes)):
            
            for ingrd in ingredients[i]:
                indegree[recipes[i]] += 1
                dict_ing[ingrd].append(recipes[i])
    
        print(dict_ing , indegree)
        
        
        queue = deque(supplies)
        
        while queue :
            
            supply = queue.popleft()
            
            for recipe in dict_ing[supply]:
                
                
                indegree[recipe] -= 1
                
                if indegree[recipe] == 0:
                    
                    queue.append(recipe)
        
        ans = []
        
        for num in indegree:
            if  not indegree[num]:
                ans.append(num) 
                
        return ans
                
                
            
            