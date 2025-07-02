class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closet = nums[0]
        min_distance = abs(nums[0])

        for num in nums : 
            distance = abs(num)

            if distance < min_distance or ( distance == min_distance and num > closet ) : 
                closet = num 
                min_distance  = distance 

        return closet
