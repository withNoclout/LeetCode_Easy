class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        freq = {}
        pairs = 0 

        for a , b in dominoes :
            key = tuple ( sorted ( [ a ,b ]))
            pairs += freq.get( key , 0 )
            freq[key] = freq.get( key , 0 ) + 1 

        return pairs 
