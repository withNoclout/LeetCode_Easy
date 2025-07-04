class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count =  0
        n = len(nums ) 

        num_set = set(nums) 

        for j in range( 1, n- 1) :
            if ( nums[j] - diff ) in num_set and ( nums[j] + diff) in num_set : 
                count += 1 

        return count 
