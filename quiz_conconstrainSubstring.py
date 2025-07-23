class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s )
        total = 0 
        for i in range(n)  :
            zeros  = ones = 0 
            for j in range( i, n ) :
                if s[j] == '0' :
                    zeros += 1 

                else : 
                    ones +=1 
                if zeros <= k or ones <= k :
                    total += 1 
                else :
                    break 

        return total
