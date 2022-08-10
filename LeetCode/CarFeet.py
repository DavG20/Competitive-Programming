class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position,speed)) #based on position
        times = [(target-p)/s for p,s in cars]
        fleet = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                fleet += 1
            else:
                times[-1] = lead
        return fleet + len(times)
