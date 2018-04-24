class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r = 0,num
        while l <= r:
            if num == 1:
                return True
            m = (l + r) // 2
            if m * m <= num < (m + 1)*(m + 1):
                ans = m
                break
            elif m * m > num:
                r = m
            else:
                l = m
        if ans * ans == num:
            return True
        else:
            return False
