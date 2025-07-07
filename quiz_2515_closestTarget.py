class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len( words  ) 
        if target not in words :
            return - 1 
        
        min_distance = n 

        for i in range(n) :
            if words[i] == target :
                dist1 = abs( i - startIndex) 
                dist2 = n - dist1 

                min_distance = min( min_distance , dist1 , dist2 ) 

        return min_distance
