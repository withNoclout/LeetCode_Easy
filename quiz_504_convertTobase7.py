class Solution( object ) : 
    def convertToBase7( self , num ):
        if num == 0 : 
            return "0" 
        
        negative  = num < 0 
        num = abs(num)
        result = ''
        while num > 0 :
            digit = num %  7 
            result = str(digit ) + result 
            num //= 7  

        return '-' + result if negative else result
