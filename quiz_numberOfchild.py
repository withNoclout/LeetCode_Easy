class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        pos = 0 
        direction = 1 
        for  _ in range(k)  :
            pos += direction 

            if pos == n -1 or pos == 0  : 
                direction = - direction 

        return pos 
