class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        i  = 1 

        while i < len(nums) - 1 : 
            left = i - 1 
            while left > 0 and nums[left ] == nums[i] : 
                left -= 1 

            right = i + 1 
            while right < len(nums) and nums[right] == nums[i] :
                right += 1 
            
            if left >= 0 and right < len(nums) :
                if nums[i] > nums[left] and nums[i] > nums[right ] :
                    count += 1 
                elif nums[i] < nums[left] and nums[i] < nums[right ] :
                    count += 1 

            i = right 

        return count 
