class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) // 2 
        freq = {}
        for num in nums : 
            freq[num]  = freq.get(num , 0 ) + 1 
            if freq[num ] > 2 : 
                return False 
        return True 
