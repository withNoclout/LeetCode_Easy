class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1 or numRows >= len(s)  :
            return s 
        
        res = [''] * numRows 
        current_row  , going_down = 0 , False 

        for char in s : 
            res[current_row] += char 
            if current_row == 0 or current_row == numRows - 1: 
                going_down = not going_down 
            current_row += 1 if going_down else -1 

        return ''.join(res) 
