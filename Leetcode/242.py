class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = dict(), dict()
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        
        for c in t:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
        
        if dict1 == dict2:
            return True
        else:
            return False

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = dict()
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        
        for c in t:
            if c in dict1:
                dict1[c] -= 1
            else:
                return False
        
        for val in dict1.values():
            if val != 0:
                return False
        return True
            
