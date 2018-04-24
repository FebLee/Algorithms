class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        sum1 = sum(nums)
        return sum1 - len(nums) * min_num
