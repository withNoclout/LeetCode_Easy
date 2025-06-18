class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s )
        result = [''] * n 
        for i in range(n) : 
            result[indices[i]] = s[i] 
        return ''.join(result)
