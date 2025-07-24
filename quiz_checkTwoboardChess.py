class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        def get_color( self , coordinate1 , coordinate2 ):
            row1, col1 = ord(coordinate1[0]) - ord('a'), int(coordinate1[1]) - 1
            row2, col2 = ord(coordinate2[0]) - ord('a'), int(coordinate2[1]) - 1
            return (row1 + col1) % 2 == (row2 + col2) % 2  
        

        return get_color(self, coordinate1, coordinate2)
