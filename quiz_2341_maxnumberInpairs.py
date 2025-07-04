class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        leftovers = 0 
        for num in nums : 
            freq[num ] = freq.get(num , 0 ) + 1 


        for count in freq.values() : 
            pairs += count // 2
            leftovers  += count % 2 

        return [ pairs , leftovers ]
