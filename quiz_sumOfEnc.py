class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0 
        for num in nums : 
            max_d = max(str(num) ) 
            en_c = int( max_d  * len(str(num ) ) ) 
            total += en_C 

        return total 
