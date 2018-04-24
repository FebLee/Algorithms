# solution of leetcode 167,two sum of a sorted array
def two_sum2(nums, target):
    '''nums type : list
       target type: int
       rtype: list, 1 based index
       '''
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if target == sum:
            return [left + 1, right + 1]
        elif target > sum:
            left += 1
        else:
            right -= 1
