class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        id_sum = {}

        for id_val , val in nums1 : 
            id_sum[id_val] = id_sum.get( id_val , 0 ) + val 

        for id_val , val in nums2 : 
            id_sum[id_val] = id_sum.get(id_val , 0  ) + val 

        result = [[id_val] , val   for id_val , val in id_sum.items()]
        result.sort( ket = lambda x: x[0]  ) 

        return result
