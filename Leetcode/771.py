class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_dict= dict()
        for c in J:
            if c in j_dict:
                j_dict[c] += 1
            else:
                j_dict[c] = 1
        count = 0
        for c in S:
            if c in j_dict:
                count += 1
        return count
