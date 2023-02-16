
def sol():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        r = 0
        answer = []
        while r < n:
            num = - float('inf')
            l = r
            while l < n and nums[l]*nums[r] > 0:
                num = max(num, nums[l])
                l += 1
            res.append(num)
            r = l
            
        print(sum(res))
sol()