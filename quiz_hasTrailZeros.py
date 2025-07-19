
class Solution :
    def hasTrailingZeros( self , nums):
        return sum(1 for num in nums if num % 2 == 0) >= 2
