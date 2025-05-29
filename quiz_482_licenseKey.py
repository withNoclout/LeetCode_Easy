class Solution( object) :
    def licenceKeyFormatting( self , s , k ) :
        s = s.replace("-" , "").upper()
        result = [] 

        for i in range(len(s)):
            if i >  0 and i % k == 0 :
                result.append("-")
            result.append(s[-(i+1)])

        return ''.join(result[::-1])
