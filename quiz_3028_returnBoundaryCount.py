class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position =  0 
        count =  0 
        for num in nums : 
            position += num 
            if position == 0 : 
                count += 1 
        return count 
