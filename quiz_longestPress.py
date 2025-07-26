class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        max_time  = 0 
        min_index  = float('inf' ) 
        prev_time = 0  

        for index , time in events : 
            curr_time = time - prev_time 
            if curr_time > max_time or ( curr_time == max_time and index < min_index  ) :
                max_time = curr_time 
                min_index = index 
            prev_time  = time 

        return min_index 
