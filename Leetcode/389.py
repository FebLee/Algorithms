class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dictionary = {}
        for char in t:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        for char in s:
            dictionary[char] -= 1
            if dictionary[char] == 0:
                del dictionary[char]
        
        for char in dictionary:
            return char
