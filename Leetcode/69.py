class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x 
        while l <= r:
            if x == 1:
                return x
            mid =  (l + r) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                r = mid 
            else:
                l = mid 
