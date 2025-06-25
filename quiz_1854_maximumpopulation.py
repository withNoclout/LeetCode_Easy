class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        delta = [0] * 101 
        for birth , death in logs : 
            delta[ birth - 1950 ] += 1 
            delta[ death - 1950 ] -= 1 

        max_pop = 0  
        curr_pop = 0 
        max_year   = 1950 

        for year in range(101 ) : 
            curr_pop += delta[year] 

            if curr_pop > max_pop : 
                max_pop = curr_pop
                max_year = 1950 + year 
        return max_year
