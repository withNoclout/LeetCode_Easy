class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()  # Sort the array first
        averages = set()  # Set to store distinct averages
        
        while nums:
            min_num = nums.pop(0)  # Remove the minimum element
            max_num = nums.pop()   # Remove the maximum element
            averages.add((min_num + max_num) / 2)  # Calculate and add the average
        
        return len(averages)  # Return the number of distinct averages
