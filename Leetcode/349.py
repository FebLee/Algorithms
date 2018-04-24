class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

    #solution 2
    def intersection(nums1,nums2):
        com_list = []
        for item in nums1:
            if item not in com_list and item in nums2:
                com_list.append(item)

        return com_list
