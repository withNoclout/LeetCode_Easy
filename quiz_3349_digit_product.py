class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(num ) : 
            product = 1 
            while num > 0 :
                digit = num % 10 
                if digit == 0 :
                    return 0 
                product *= digit 
                num //= 10 
            return product 
        num = n 
        while True :
            if digit_product(num) % t == 0 :
                return num 
            num += 1 

            
