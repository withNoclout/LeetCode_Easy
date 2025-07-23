class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s) 
        result  = [] 

        for i in range(n) : 
            new_index = ( i + k ) % n 
            result.append(s[new_index] ) 

        return ''.join(result)
