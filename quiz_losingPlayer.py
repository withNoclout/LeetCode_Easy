class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        turns = min(x,y //4 ) 
        return 'Alice' if turns %2 ==1 else 'Bob' 
    
    
