class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_s = "" 
        for num in digits : 
            new_s += str(num) 
        new_i = int(new_s) + 1 
        return [ int(i) for i in str(new_i)] 
