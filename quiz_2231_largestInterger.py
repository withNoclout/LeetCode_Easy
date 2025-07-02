class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num )) 
        even_digits = []
        odd_digits = []

        for i, digit in enumerate(digits) : 
            d = int(digit )
            if d %2 == 0 :
                even_digits.append((d , i) ) 
            else : 
                odd_digits.append((d,i ) ) 

        even_digits.sort(reverse=True) 
        odd_digits.sort(reverse=True ) 

        result = ['' ] * len(digits)
        even_idx = 0 
        odd_idx = 0 
        for i in range( len( digits ))  :
            if int( digits[i] ) % 2  ==  0 : 
                result[i]  = str( even_digits[even_idx][0])
                even_idx += 1 
            else : 
                result[i] = str(odd_digits[odd_idx ][0])
                odd_idx += 1 

        return int(''.join(result))
