class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the index for the next unique element
        unique_index = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Assign it to the unique index and increment the index
                nums[unique_index] = nums[i]
                unique_index += 1

        # Return the length of the unique elements
        return unique_index
    
    
