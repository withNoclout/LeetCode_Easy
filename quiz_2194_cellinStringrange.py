class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        col1 ,row1  = s[0] , int(s[1:s.find(':')])
        col2 , row2 = s[s.find(':')+1]  , int(s[s.find(':')+2 : ] )

        result = []

        for col in range( ord(col1)  , ord(col2 ) + 1 ) :
            for row in range( row1 , row2 + 1 ) :
                result.append( chr(col) + str(row)) 

        return result
