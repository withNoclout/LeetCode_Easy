class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        point = set()

        for start , end in nums : 
            for i in range( start , end+ 1 ): 
                point.add(i) 

        return len(point)
