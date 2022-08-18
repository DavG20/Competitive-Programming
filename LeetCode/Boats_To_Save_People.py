class Solution(object):
    def numRescueBoats(self,people,limit):
        start = 0
        end = len(people) - 1

        people.sort()

        while start <= end:
            remain_cap = limit - people[end]
            end -= 1
            if people[start] <= remain_cap:
                start += 1
            ans += 1

        return ans
            