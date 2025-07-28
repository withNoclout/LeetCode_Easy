class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits  = [ int(d) for d in str(n) ] 
        digits_sum = sum(digits)

        digits_product = 1 

        for d in digits : 
            digits_product *= d if d != 0 else 1
        return digits_product % digits_sum == 0 and digits_sum % 2 == 0
