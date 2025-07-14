class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd( a ,b ) :
            while b :
                a ,b = b , a % b 
            return a 
        
        count = 0 
        n = len(nums) 

        for i in range(n) :
            for j in range(i + 1 , n ) :
                first = int(str(nums[i])[0])
                last = int(str(nums[j])[-1])

                if gcd( first, last ) == 1 :
                    count += 1 

        return count
