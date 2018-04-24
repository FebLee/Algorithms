class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = dict()
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        
        for letter in s:
            t_dict[letter] -= 1
            if t_dict[letter] == 0:
                del t_dict[letter]
            
        for key in t_dict.keys():
            return key
