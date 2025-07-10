class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def is_prime( n ) :
            if n < 2 : 
                return False 
            for i in range( 2 , int( n** 0.5 ) + 1 ) :
                if n % i == 0 : 
                    return False 
            return True 
        
        n = len(nums) 
        max_prime = 0 

        for i in range(n) :
            for val in ( nums[i][i] , nums[i][n-i-1 ] ) :
                if is_prime(val ) :
                    max_prime = max( max_prime , val ) 

        return max_prime
