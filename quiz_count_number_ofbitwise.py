class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0 
        count = 0

        def dfs( i , curr ) :
            nonlocal max_or , count 
            if i == len( nums)  :
                if curr == max_or : 
                    count += 1 

                elif curr > max_or : 
                    max_or = curr 
                    count = 1 

                return 
            dfs( i + 1 , curr | nums[i] )
            dfs( i + 1 , curr )
        dfs( 0 , 0 )
        return count 
