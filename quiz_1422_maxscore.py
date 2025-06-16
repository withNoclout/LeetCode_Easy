class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score =  0 
        for i in range( 1, len(s ) ) :
            left = s[:i]
            right = s[i: ] 

            left_zeros  = left.count('0')

            right_ones  = right.count('1')

            max_score = max( max_score  , left_zeros + right_ones)  

        return max_score 
