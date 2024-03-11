import math


class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v

    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)

    def valid(self):
        '''True if both u and v are integers.'''
        return isinstance(self.u, int) and isinstance(self.v, int)

    def gcd(self):
        '''Compute the greatest common divisor of member variables u and v.'''
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
    # 0,0 case check
        if self.u == 0 and self.v == 0:
            raise Exception("GCD is undefined for two zeros")
# need numbers to be whole and postive for Euclid's Algo
        tempU = abs(round(self.u))
        tempV = abs(round(self.v))
        # implmentation of Euclid's algo
        while tempV != 0:
            tempU, tempV = tempV, tempU % tempV
        return tempU

        if OverflowError:
            print("One or both of the values are equal to infinity.")
            raise OverflowError

    def lcm(self):
        '''Compute the least common multiple of member variables u and v.'''
        # Hint: Use the gcd of a and b
        #0,0 case check
        if self.u == 0 and self.v == 0:
            raise Exception("LCM is undefined for two zeros")
        tempU = abs(round(self.u))
        tempV = abs(round(self.v))
        gcd = self.gcd()
        # lcm of 2 numbers a and b= (a*B)/gcd(a,b)
        lcm = (tempU * tempV) // gcd
        if OverflowError:
            print("one or both the values of ", tempU, " and ", tempV, " are equal to infinity")
            raise OverflowError
        return lcm

