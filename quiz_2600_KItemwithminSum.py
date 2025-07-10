class Solution(object):
    def kItemsWithMawximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        take_one = min(numOnes , k  )
        k -= take_one
        result = take_one

        take_zero = min( numZeros , k )

        k -= take_zero

        result -= k 

        return result 
