class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies) 

        return [ candies[i] + extraCandies >= max_candies for i in range(len(candies )) ]
