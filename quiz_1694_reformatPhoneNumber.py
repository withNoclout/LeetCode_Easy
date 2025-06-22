class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digit = ''.join( c for c in number if c.isdigit()) 
        result = [] 
        i = 0 
        while i < len(digit):
            if len(digit) - i == 4:
                result.append(digit[i:i+2])
                result.append(digit[i+2:i+4])
                break
            elif len(digit) - i == 3:
                result.append(digit[i:i+3])
                break
            else:
                result.append(digit[i:i+3])
            i += 3

        return '-'.join(result)
