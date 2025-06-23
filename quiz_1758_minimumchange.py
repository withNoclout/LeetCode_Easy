class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        alt1  = alt2 = 0 
        for i , ch in enumerate(s ) :
            if ch != str( i % 2 ) :
                alt1 +=  1 
            if ch !=  str( (i+1 ) %2 )  :
                alt2 += 1
        return min(alt1, alt2)
