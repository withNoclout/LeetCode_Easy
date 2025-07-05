class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_ops = float('inf')

        for i in range( len(blocks) - k  + 1 ) :
            white_count = blocks[i:i+k].count('W')
            min_ops = min( min_ops , white_count ) 


        return min_ops 
        
