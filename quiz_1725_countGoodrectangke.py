class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_length = 0
        count = 0
        for length , width in rectangles : 
            curr_len = min( length , width ) 
            if curr_len > max_length : 
                max_length = curr_len
                count = 1 
            elif curr_len == max_length : 
                count += 1 
        return count 
