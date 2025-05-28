class Solution( object)  : 
    def findDifference( self , s , t ) :
        result = 0 
        for char in s+ t : 
            result ^= ord(char)
        return char(result)
