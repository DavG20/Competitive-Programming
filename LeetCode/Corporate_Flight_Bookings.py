import numpy as np
class Solution(object):
    def corpFlightBookings(self,bookings,n):
        res=np.array([0]*n ) #did'nt pass the time limit  with out the out numpy package

        for flight in bookings:
            ranges=flight[1]-flightp[0]
            if ranges==0:
                res[flight[0]-1]+=flight[2]
            else:
                res[flight[0]-1:flight[1]]+=flight[2]
        return res 
