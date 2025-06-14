class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [] 

        for i in range( 0 ,  len(_nums ) , 2 )  :
            freq  = nums[i] 
            val = nums[ i +1 ] 

            result.extend([val ] * frq ) 

        return result
