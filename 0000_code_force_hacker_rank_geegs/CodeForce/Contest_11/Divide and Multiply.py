t = int(input())

for _ in range(t):

    n =int(input())

    nums = list(map(int , input().split()))
    
    even = []
    odd =[]
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    even.sort()
    if len(nums) == len(even):
        odd.append(even.pop())
    else:
        for num in nums:
            if num % 2:
                odd.append(num)
    odd.sort()

    left = 0 

    while left < len(even) :
        even[left] = even[left]//2

        if even[left] == 1:
            left += 1
        odd[-1] *=2
    print(sum(odd) + sum(even))


