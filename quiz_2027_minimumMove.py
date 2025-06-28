class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        move = 0 
        i = 0 
        while i < len(s) : 
            if s[i] =='X':
                move += 1 
                i += 3 

            else : 
                i += 1 

        return move 
