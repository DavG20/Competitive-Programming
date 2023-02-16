class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = l = 0
        while l + 2 < n:
            r = l + 1
            if arr[l] < arr[l + 1]:
                while r + 1 < n and arr[r] < arr[r + 1]:
                    r += 1
                if r < n - 1 and arr[r] > arr[r + 1]:
                    while r + 1 < n and arr[r] > arr[r + 1]:
                        r += 1
                    res = max(res, r - l + 1)
                else:
                    r += 1
            l = r
        return res