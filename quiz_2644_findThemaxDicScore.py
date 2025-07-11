class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        max_scores =  -1 
        result = min(divisors)

        for d in divisors : 
            score = sum ( 1 for num in nums if num % d == 0 )

            if score > max_scores : 
                max_scores = score 
                result = d 

            elif score == max_scores : 
                result = min( result , d )

        return result 
