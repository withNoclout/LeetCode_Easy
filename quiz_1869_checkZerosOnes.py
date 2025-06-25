class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_ones  = max_zeros = curr_ones = curr_zeros = 0 

        for char in s : 
            if char == '1' : 
                curr_ones += 1 
                curr_zeros = 0 
                max_ones = max( max_ones , curr_ones  )

            else : 
                curr_zeros += 1 
                curr_ones =  0 
                max_zeros = max( max_zeros , curr_zeros ) 

        return max_ones > max_zeros  
