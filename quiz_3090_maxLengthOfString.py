class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len =  0 
        for i in range(len(s) )  :
            freq = {}
            for j in range( i , len(s) ) :
                freq[s[j] ] = freq.get( s[j] ,  0 ) + 1 
                if freq[s[j]] > 2 : 
                    break 

                max_len = max( max_len , j-  i + 1 )

        return max_len 
