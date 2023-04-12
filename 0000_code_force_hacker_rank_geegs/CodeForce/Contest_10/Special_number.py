t = int(input())
 
 
for _ in range(t):
    
    
    n , k = list(map(int , input().split()))
    
    count = 0 
    
    ans = ((k >> 0) & 1) 
    
    # print(ans)
    while k :
        
        count += 1
        if (k >> 1) & 1:
            ans += n ** count 
        k >>= 1
    print(ans % ((10**9 )+ 7))
    