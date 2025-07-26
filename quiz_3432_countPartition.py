class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        count = 0 
        left_sum = 0 
        for i in range( len(nums)  - 1 ) : 
            left_sum += nums[i] 
            right_sum = total - left_sum 
            if ( left_sum % 2 ) == ( right_sum % 2 ) :
                count += 1
        return count
