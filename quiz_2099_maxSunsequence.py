class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        index_nums = [ ( num ,  i ) for i , num in enumerate(nums) ] 

        index_nums.sort(reverse=True ) 

        top_k = index_nums[:k]
        top_k.sort( key = lambda x: x[1])

        return [num for num , _ in top_k]
