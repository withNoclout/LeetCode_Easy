class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        actual_set_sum = sum(set(nums))
        
        dup = actual_sum - actual_set_sum
        missing = expected_sum - actual_set_sum

        return [dup, missing]
