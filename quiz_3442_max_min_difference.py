class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for char in s : 
            freq[char ] = freq.get( char , 0 ) + 1 

        max_odd = 0 
        max_even = float('inf')

        for count in freq.values(): 
            if count % 2 == 1 :
                max_odd = max( max_odd , count ) 

            else : 
                max_even = min( max_even , count ) 

        return max_odd - max_even if max_odd > 0 and max_even < float('inf') else -1
