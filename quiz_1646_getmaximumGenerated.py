class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 : 
            return 0 
        if n == 1 : 
            return 1 
        
        nums = [0] * ( n + 1 ) 
        nums[1] = 1 
        max_val = 1 

        for i in range( 1, (n+1 )// 2 ) :
            nums[2* i ] = nums[i] 
            max_val = max( max_val , nums[2 * i ]) 

            if 2 * i + 1 <= n : 
                nums[ 2 * i + 1 ]  = nums[i] + nums[i+ 1] 
                max_val = max( max_val , nums[2 * i + 1 ])

        return max_val  
