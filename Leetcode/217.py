class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] >= 2:
                    return True
            else:
                d[num] = 1
        return False
