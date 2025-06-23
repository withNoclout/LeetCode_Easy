class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        count  = Counter(nums)

        return sum(num for num, freq in count.items() if freq == 1)
