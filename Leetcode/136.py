class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key, val in d.items():
            if val == 1:
                return key


    #2. math solution
        return 2 * sum(set(nums)) - sum(nums)
