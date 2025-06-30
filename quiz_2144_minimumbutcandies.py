class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reversed=True)

        total_cost = 0 

        for i in range( 0 , len(cost ) ,3 ) :
            total_cost += sum(cost[i:i+2] )

        return total_cost 
