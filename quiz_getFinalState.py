class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for _ in range(k)  :
            min_val = min(nums ) 
            for i in range( len(nums ) ) :
                if nums[i] == min_val : 
                    nums[i] *= multiplier
                    break 

        return nums 
