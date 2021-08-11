# Square root of a number without using in-built exponent function or operators
# Note: Truncate result to return only integer part

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int     
        """
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2

        print(int(result))
        return int(result)
        
