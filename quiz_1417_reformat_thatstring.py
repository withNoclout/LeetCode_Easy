class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = [ c for c in s if c.isalpha()]
        digits =  [ c for c in s if c.isdigit()]

        if abs( len(letters) - len(digits)) > 1 : 
            return "" 
        
        result = [] 

        if len(letters ) >= len(digits) : 
            for i in range(len(digits ) ) :
                result.append(letters[i])
                result.append( digits[i])
            if len(letters) > len(digits ) : 
                result.append(letters[-1])
        else : 
            for i in range(len(letters) ) :
                result.append(digits[i])
                result.append(letters[i])
            if len(digits ) > len(letters ) : 
                result.append(digits[-1])

        return "".join(result)
