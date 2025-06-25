class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_distance= float('inf')
        for i in range( len(nums ) ) :
            if nums[i] == target : 
                distance = abs( i - start ) 
                min_distance = min( min_distance , distance)

        return min_distance 
