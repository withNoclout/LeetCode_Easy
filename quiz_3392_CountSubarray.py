class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        n =len(nums ) 
        for i in range(n - 2 ) :
            if nums[i+1 ] % 2 == 0 : 
                if nums[i] + nums[i+2 ] == nums[i+1 ] // 2 :
                    count +=  1 
        return count + n   
