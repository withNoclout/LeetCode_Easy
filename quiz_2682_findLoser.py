class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        seen = set()
        curr= 1 
        i= 1 

        while curr not in seen :
            seen.add( curr) 
            curr = ( curr + i * k - 1 ) % n + 1 

            i += 1 

        losers = [ i for i in range(1 , n+1 ) if i not in seen ] 

        return losers 
