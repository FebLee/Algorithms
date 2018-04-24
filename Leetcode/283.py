class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
       
        if i == len(nums) - 1:
            return

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                break
            j += 1
        
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
            
