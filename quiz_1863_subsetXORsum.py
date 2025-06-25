class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack( index , curr_xor ) : 
            if index == len(nums) : 
                return curr_xor 

            include = backtrack( index + 1 , curr_xor ^ nums[index ] ) 
            exclude = backtrack( index + 1 , curr_xor ) 
            return include + exclude
        
        return backtrack( 0 , 0 )
