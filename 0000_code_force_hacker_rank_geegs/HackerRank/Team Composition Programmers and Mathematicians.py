def sol(programmers , mathematician , teams):
    
    start = 0 
    
    end = teams 
    
    num_team = 0
    
    while start <= end:
        
        mid = start + (end - start ) // 2
        
        remainder = programmers - mid + mathematician - mid 
        
        if  remainder >= 2 * mid:
            
            num_team = mid  
            
            start = mid + 1
        else :
            
            end = mid - 1
            
    return num_team

t = int(input())

for _ in range(t):
    
    a , b = list(map(int, input().split()))
    
    teams = min(a ,b)
    
    team = sol(a, b, teams)
    
    print(team)
        