class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def is_prime(num):
            if num < 2 : 
                return False 
            
            for i in range(2 , int(num ** 0.5 ) + 1 ) :
                if num % i == 0 :
                    return False
            return True
        

        from collections  import Counter 
        freq = Counter(nums ) 

        for count in freq.values() : 
            if is_prime(count ) :
                return True 
            
        return False 
