class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len( word ) 
        if n <= 8 : 
            return n 
        freq = sorted([ word.count(c) for c in set(word)] , reverse=True) 

        total_pushes  = 0 
        for i , count in enumerate(freq  ) :
            total_pushes += count * ( i // 8 + 1 ) 
        return total_pushes 
