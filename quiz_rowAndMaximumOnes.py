class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_ones = 0 
        max_row = 0 

        for i in range(len(mat) ) :
            ones = sum(mat[i])
            if ones > max_ones :
                max_ones = ones 
                max_row = i 


        return [ max_row , max_ones ]
