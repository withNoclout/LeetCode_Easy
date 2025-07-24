class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {} 
        for num in nums : 
            freq[num ]  = freq.get(num , 0 ) + 1 

        result = []

        for num , count in freq.items() : 
            if count == 2 : 
                result.append(num ) 


        return result 
