class Solution : 
    def numberGame( self , nums):
        nums.sort()  # Sort the array in ascending order
        arr = []
        for i in range(0, len(nums), 2):
            # Bob appends the second smallest (nums[i+1]), then Alice appends the smallest (nums[i])
            arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr
