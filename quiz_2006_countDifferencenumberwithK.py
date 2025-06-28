class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0 
        freq = {}

        for num in nums : 
            freq[num] = freq.get(num , 0 ) + 1 

        for num in freq : 
            if num+ k in freq : 
                count += freq[num] * freq[num + k ]

        return count 
