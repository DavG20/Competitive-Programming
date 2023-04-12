n , k = list(map(int, input().split()))

if n < k:
    print("NO")
elif n == k:
     print("YES")
     arr = [1] * n
     print(*arr)
else:
    count = (n >> 0) & 1
    if count :
        ans = [1]
    else:
        ans = []
        count = 1

    while n:
        if (n >> 1) & 1 :
            ans.append(2 ** count )
        count += 1
        n >>= 1
    i = 0
    while len(ans) < k and i < len(ans):
        if ans[i] != 0 :
            val = ans.pop(ans[i])
            if len(ans) + 1 < k and val > 1:
                    ans.append(val // 2)
                    ans.append(val // 2)
            else:
                    break
        else:
                i += 1
    if len(ans) == k:
        print("YES")
        print(*ans)
        
    else:
        print("NO")





