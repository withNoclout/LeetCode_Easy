class Solution( object ) : 
    def repeatedSubStringPattern( self , s ) :
        doubled = ( s + s )[1:-1] 
        return s in doubled  
