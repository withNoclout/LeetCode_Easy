class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid_nums = [ num for num in nums if num % 2 == 0 and num %3 == 0 ]

        return sum( valid_nums ) // len( valid_nums ) if valid_nums else 0 
