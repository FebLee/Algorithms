class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            while left <= right:
                if temp_list[left] in ('aeiouAEIOU'):
                    break
                left += 1
            
            while right >=left:
                if temp_list[right] in ('aeiouAEIOU'):
                    break
                right -= 1
            
            if left < right:
                temp_list[left],temp_list[right] = temp_list[right],temp_list[left]
            
            left += 1
            right -= 1
        
        return ''.join(temp_list)


# solution-2
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list = list(s)
        left = 0
        right = len(s) - 1
        find_l = False
        find_r = False
        while left < right:
            if temp_list[left] not in ('aeiouAEIOU'):
                left += 1
            else:
                find_l = True
            if temp_list[right] not in ('aeiouAEIOU'):
                right -= 1
            else:
                find_r = True
            if (find_l and find_r):         
                temp_list[left],temp_list[right] = temp_list[right],temp_list[left]
                left += 1
                right -= 1
                find_l = False
                find_r = False
        
        return ''.join(temp_list)

#solution-3:

    class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        temp_list = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if temp_list[left] not in vowels:
                left += 1
            if temp_list[right] not in vowels:
                right -= 1
            if (temp_list[left] in vowels and temp_list[right] in vowels):         
                temp_list[left],temp_list[right] = temp_list[right],temp_list[left]
                left += 1
                right -= 1
        
        return ''.join(temp_list)
