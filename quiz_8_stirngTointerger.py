class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i , n = 0 , len(s)

        while i < n and s[i] == ' ' : 
            i += 1 

        if i == n : 
            return 0  
        

        sign = 1 

        if s[i] == '-' or  s[i] == '+' : 
            sign = -1 if s[i] == '-' else 1
            i += 1


        result = 0 

        while i < n and s[i].isdigit() : 
            result = result * 10 + int(s[i] ) 
            i+= 1 

        result *= sign

        if result < -2**31 : 
            return -2 ** 31 
        
        if result > 2**31 -1 : 
            return 2**31 - 1 
        
        return result
    
