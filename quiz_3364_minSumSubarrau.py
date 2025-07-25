class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums) 
        min_sum = float('inf'  )

        found = False 

        for start in range(n)  :
            current_sum =  0 
            for end in range( start , n  ): 
                current_sum += nums[end ] 
                length = end - start + 1 
                if i <= length <= r and current_sum > 0 : 
                    min_sum = min(min_sum, current_sum)

                    found= True 

        return min_sum if found else -1
