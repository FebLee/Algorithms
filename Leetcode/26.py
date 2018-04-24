class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        i = 1
        pre = nums[0]
        while i < len(nums):
            if nums[i] == pre:
                break
            else:
                pre = nums[i]
            i += 1

        if i == len(nums) -1:
            if nums[i] == pre:
                return i
            else:
                return i + 1

            
        j = i + 1
        while j < len(nums):
            if nums[j] != pre:
                break
            j += 1
        
        while j < len(nums):
            if nums[j] == pre:
                j += 1
            elif nums[j] != pre:
                pre = nums[j]
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
        
        
        size = len(nums)
        for k in range(size - i):
            nums.pop()
        return i
