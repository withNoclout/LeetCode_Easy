class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Count frequency of each number (0 to 100)
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
        
        # Compute cumulative sum to get count of smaller numbers
        for i in range(1, 101):
            freq[i] += freq[i-1]
        
        # Map each number to count of smaller numbers
        return [freq[num-1] if num > 0 else 0 for num in nums]
