class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums : 
            if num % 2 == 0 :
                freq[num ] = freq.get(num , 0 ) + 1 

        if not freq :
            return  -1 
        

        max_freq = max( freq.values() ) 
        return min(num for num, count in freq.items() if count == max_freq)
