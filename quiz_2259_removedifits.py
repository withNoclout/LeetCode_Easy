class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        max_result = ' ' 

        for i in range(len(number ) ) : 
            if number[i] == digit : 
                new_num = number[:i] + number[i+1: ] 
                max_result = max( max_result , new_num  ) 


        return max_result
