class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        strengths = [( sum(row ) ,  i ) for i  , row in enumerate(mat ) ] 

        strengths.sort()

        return [ index for _ , index in strengths[:k]]
