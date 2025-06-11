class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ann = [0] * num_people
        give = 1 
        i = 0 

        while candies > 0 : 
            ans[ i % num_people ] += min( give , candies )

            candies -= min( give , candies ) 

            give += 1  
            i+= 1 

        return ans 
