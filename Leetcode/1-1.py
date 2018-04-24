class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = dict()
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in my_dict:
                return [my_dict[num2], i]
            else:
                my_dict[nums[i]] = i
                
