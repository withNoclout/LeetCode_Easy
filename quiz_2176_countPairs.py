class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = { }
        count = 0 
        for num in nums : 
            freq[num] = freq.get(num , 0 ) + 1 

        for i in range( len(nums) ) : 
            for j in range( i+ 1 , len(nums) ) : 
                if nums[i] == nums[j] and ( i * j ) % k == 0  : 
                    count += 1 
        return count 
