class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(k)
        n = len(nums)
        
        if k == 0:
            return
        k = k % n
        nums = nums[n - k : n] + nums[:n - k]
        return nums
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(s.rotate(nums,k))
