class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter 
        freq = Counter(nums) 

        return sorted(nums, key=lambda x: (freq[x], -x))
