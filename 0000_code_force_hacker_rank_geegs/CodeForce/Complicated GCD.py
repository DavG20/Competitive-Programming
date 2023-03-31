a ,b = list(map(int , input().split()))


def GCD(a , b):

    if b == 0 :
        return a
    return GCD(b , a % b)

if b - a >= 1:

    print(1)
    
else:
    
    print(GCD(a , b))