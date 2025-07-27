class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums ) 
        if n < k :
            return -1 
        
        freq = {}
        for i in range( n - k + 1 ) :
            subarray = nums[i:i+k] 
            for num in set(sunarray ) :
                freq[num]  = freq.get(num , 0 ) + 1 


        max_num = -1 
        for num , count in freq.items() :
            if count == 1 : 
                max_num = max( max_num , num ) 

        return max_num 
