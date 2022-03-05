import math


class Theatre_Square:
    def number_of_square(self, n,m,a):
        print(math.ceil(n/a),"the rounded")
        count= (math.ceil(n/a))*(math.ceil(m/a))
        return count


