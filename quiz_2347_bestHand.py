class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if len( set( suits ) ) == 1 :
            return "Flush"
        
        rank_count = {}

        for rank in ranks :
            rank_count[rank] = rank_count.get(rank , 0) + 1 

        max_freq = max( rank_count.values()) 

        if max_freq >= 3 : 
            return "Three of a Kind"
        
        if max_freq == 2 : 
            return "Pair"
        

        return "High Card"
