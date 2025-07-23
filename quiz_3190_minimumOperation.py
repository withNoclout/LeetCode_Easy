class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0 
        for num in nums : 
            if num % 3 != 0 :
                operation += min(num % 3 , 3 - num % 3  ) 

        return operations
