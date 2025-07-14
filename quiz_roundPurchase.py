class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        round_amount = round( purchaseAmount / 10 ) * 10 
        return 100 - round_amount

