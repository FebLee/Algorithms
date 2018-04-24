class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        origin_num = x
        count = 0
        while origin_num > 0:
            origin_num = origin_num // 10
            count += 1
            
        while count >= 2:
            first = x % 10
            second = x // (10 ** (count - 1))
            if first != second:
                return False
            x = x % (10 ** (count - 1))
            x = x // 10
            count -= 2
        return True
