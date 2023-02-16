import collections


class Solution:
    def shortestSubarray(self, A, K):
        dp = [0] * (len(A) + 1)
        print(dp)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + A[i - 1]
        print("after",dp)
        res = len(A) + 1
        Q = collections.deque()
        print(Q)
        for i in range(len(dp)):
            while Q and dp[i] - dp[Q[0]] >= K:
                res = min(res, i - Q.popleft())
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop() 
            Q.append(i)

        return res if res != len(A)+1 else -1
