class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        highest_product = n % 10 
        max_prod = highest_product
        n //= 10

        while n > 0 :
            max_prod = max( max_prod , highest_product * (n % 10) )
            if n % 10 > highest_product :
                highest_product = n % 10
            n //= 10

        return max_prod
