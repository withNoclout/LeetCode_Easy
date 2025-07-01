class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        # count = 0 
        # for num in range(num) : 
        #     if num % 2 ==  1: 
        #         count += 1 
        # return count 

        total = 0 
        def digit_sum( n ) :
            while n > 0 : 
                total += n % 10 
                n //= 10 
            return total 
        
        count = 0 
        for i in range( 1, num + 1  ) :
            if digit_sum(i) % 2 == 0 :
                count += 1 
        return count 
