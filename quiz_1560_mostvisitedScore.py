class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start = rounds[0]
        end = rounds[-1]

        if start <= end  :
            return list( range( start , end + 1  ))
        
        else : 
            return list( range( start , n + 1) ) + list( range( 1, end +1 ))
