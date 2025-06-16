class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {} 
        for num in arr : 
            freq[num]  = freq.get( num , 0 ) + 1 

        lucky = -1 
        for num in freq :
            if num == freq[num ] : 
                lucky = max( lucky , num )

        return lucky
