class Solution:
    def minCosts(self, cost):
        currentCost = float('inf')
        for i in range(len(cost)):
            if currentCost > cost[i]:
                currentCost = cost[i]
            cost[i] = currentCost
        return cost
