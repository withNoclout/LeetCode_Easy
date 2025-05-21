class Solution( object ) : 
    def titleToNumber( self , columTitle ) : 
        result = 0 
        for char in columnTitle : 
            result = result *26 + ( ord( char)  -  ord('A') + 1 ) 
        return result 
