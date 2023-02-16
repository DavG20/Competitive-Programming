class Solution(object):
    def dailyTemperatures(self, T):
        length = len(T)

        res = [0] * length

        for i in range(length):
            for j in range(i+1, length):
                if T[i] < T[j]:
                    res[i] = j - i
                    break

        return ans