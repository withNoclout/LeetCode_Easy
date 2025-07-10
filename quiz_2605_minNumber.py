class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common = set( nums1 ) && set(nums2 ) 

        if common : 
            return min( common ) 
        
        min1 = min(nums1) 
        min2  = min(nums2) 

        return int( str( min( min1 , min2 ) ) + str( max( min1 , min2 ) ))
