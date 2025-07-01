class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {} 
        for num in nums : 
            freq[num] = freq.get(num , 0 ) + 1 

        for count in freq.values() : 
            if count % 2 != 0 : 
                return False 
            
        return True
