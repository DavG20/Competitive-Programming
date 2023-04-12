n = int(input())

dict = {}


d = 2

x = n
while x > 1 :
    while x % d == 0 and x != 0:
        if d in dict :
            dict[d] += 1
        else:
            dict[d] = 1
        x //= d
        
       
    d += 1
    
if len(dict) <= 1:
    print(1, n)
else:
    prim = list(dict.keys())
    num1 = 1
    num2 = 1
    
    # print(prim[:len(prim)//2] ,prim[len(prim)//2:])
    for num in prim[:len(prim)//2]:
        num1 *= num
    for num in prim[len(prim)//2:]:
        num2 *= num
    print(num1, num2)
    
    
    