class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        inside_bars = False 

        for char in s : 
            if char == '|'  :
                inside_bars = not inside_bars 
            elif char == '*' and not inside_bars : 
                count += 1 

        return count 
