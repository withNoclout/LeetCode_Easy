class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        min_len = min(len(s1), len(s2), len(s3))
        common_len = 0 
        for i in range(min_len ) :
            if s1[i] == s2[i] ==s3[i] : 
                common_len += 1
            else : 
                break 

        if common_len == 0  or common_len >= min( len(s1) , len(s2), len(s3) ) :
            return -1
        
        return len(s1) + len(s2) + len(s3) - 3 * common_len
