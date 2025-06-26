class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        coverd = set()
        for start , end in ranges : 
            for x in range( start , end+ 1) : 
                coverd.add(x) 

        for x in range( left , right + 1 ) :
            if x not in coverd : 
                return False 
            
        return True 
