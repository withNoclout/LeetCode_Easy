class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        freq = [0] * 1001 

        for num in arr1 :
            freq[num] += 1 

        result = [] 
        for num in arr2 :
            result.extend( [num ] * freq[num])
            freq[num ] = 0 

        for num in range( 1001 ) :
            if freq[num] > 0  : 
                result.extend([num] * freq[num])

        return result
