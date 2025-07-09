class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycles = time //( n-1 )
        remaining = time %( n-1)

        if cycles % 2 == 0 : 
            return remaining + 1 
        else : 
            return n - remaining 
