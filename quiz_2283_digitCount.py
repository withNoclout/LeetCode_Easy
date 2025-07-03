class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        freq = [0] * 10
        for digit in num : 
            freq[int(digit)] += 1 


        for i in range(len(num)) :
            if freq[i] != int( num[i]) :
                return False 
            
        return True
