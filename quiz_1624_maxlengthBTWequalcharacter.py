class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        max_length = -1 

        for i , char in enumerate(s ) :
            if char not in first : 
                first[char]  = i  
            else : 
                max_length  = max( max_length , i - first[char] - 1  ) 
        return max_length
