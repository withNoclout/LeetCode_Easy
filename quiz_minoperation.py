class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_sum = sum(nums)

        remainder = total_sum % k 
        if remainder == 0 :
            return 0 
        return remainder 
