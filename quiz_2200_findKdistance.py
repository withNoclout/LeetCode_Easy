class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        key_indices = [ j for j in range(len(nums ) ) if nums[j] == key ] 

        result = set()

        for j in key_indices : 
            for i in range( max( 0 , j - k ) , min( len(nums) , j + k + 1 ) ): 
                result.add(i)

        return sorted( list(result))
