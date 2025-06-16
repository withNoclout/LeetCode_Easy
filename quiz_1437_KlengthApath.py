class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev_one = -k - 1 
        for i in range( len(nums)  ) :
            if nums[i] == 1  : 
                if i - prev_one - 1 < k : 
                    return False 
                prev_one = i 
        return True 
