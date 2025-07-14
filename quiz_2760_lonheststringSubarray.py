class Solution : 
    def longestAlternatingSubarray(self , nums, threshold):
        max_length = 0
        n = len(nums)
        
        for l in range(n):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l
                while r < n and nums[r] <= threshold:
                    if r > l and nums[r] % 2 == nums[r-1] % 2:
                        break
                    max_length = max(max_length, r - l + 1)
                    r += 1
        
        return max_length
