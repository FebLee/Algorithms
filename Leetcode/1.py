# solution of leetcode 1
def two_sum(nums, target):
    '''nums type: list
       target type: int
       rtype: list
       '''
    value_index_pairs = dict()
    for i in range(len(nums)):
        another_num = target - nums[i]
        if another_num in value_index_pairs:
            return [value_index_pairs[another_num], i]
        else:
            value_index_pairs[nums[i]] = i
