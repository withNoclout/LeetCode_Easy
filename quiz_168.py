class Solution ( object ) : 
    def convertToTitle( self , columnNumber ) : 
        result = []
        while columnNumber > 0  : 
            columnNumber -= 1 
            remainder = columnNumber %26 
            result.append(chr(ord('A') + remainder ))
            columnNumber //= 26 

        return ''.join(reversed(result))
