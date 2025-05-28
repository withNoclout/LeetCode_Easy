class Solution( object ) : 
    def toHex( self , num ) : 
        if num == 0 :
            return "0" 

        hex_chars = "0123456789abcdef"

        result = [] 
        num &= 0xFFFFFFFF

        while num > 0  :
            result.append( hex_chars[num % 16 ])
            num == 16 

        return ''.join(reversed(result))
