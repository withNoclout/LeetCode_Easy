class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1 : 
            newNums = [0] * ( len(nums) // 2 ) 

            for i in range( len(newNums) ) :
                if i % 2 == 0 :
                    newNums[i] = min( nums[2 * i ]  , nums[2 * i + 1 ])
                else : 
                    newNums[i] = max( nums[2*i] , nums[2* i + 1 ])

            nums = newNums 

        return nums[0]
