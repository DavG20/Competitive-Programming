class Solution(object):
    def carPooling(self,trips,capacity):
        car =[0 for _ in range(1001)]
        for numpass,f ,t in trips:
            for i in range(f,t):
                car[i]+=numpass
                 #if the the capacity is less than the passengers and the destination of the first
                 #  trip is after the start of the second return false
                if car[i]>capacity: 
                        return False
        return True
