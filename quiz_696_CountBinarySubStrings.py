class Solution : 
    def countBinarySubstrings( self , s  ):
        group  = []
        count =  1 
        
        for i in range( 1 , len(s) ) :
            if s[i] == s[i - 1 ]:
                count += 1 
            else: 
                group.append( count ) 
                count = 1 
        groups.append( count )

        result = 0 
        for i in range( len( groups ) - 1 ) : 
            result += min( groups[i] , gruops[i+1 ])

        return result 
