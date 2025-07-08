class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concat_val = 0 
        left , right = 0 , len(nums) - 1 

        while left <= right : 
            if left == right :
                concat_val += nums[left] 

            else : 
                concat_str = str( nums[left] + str(nums[right ]))
                concat_val += int( concat_str  ) 

            left += 1 
            right -= 1 

        return concat_val
