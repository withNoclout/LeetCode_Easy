class Solution : 
    def minimumRightShifts(self, nums):
        n = len(nums)
        # Find the index where sorted array starts
        for i in range(n):
            # Check if array is sorted after i shifts
            is_sorted = True
            for j in range(n-1):
                if nums[(j + i) % n] > nums[(j + i + 1) % n]:
                    is_sorted = False
                    break
            if is_sorted:
                return i
        return -1
    

# ============ GPT =====


class Solution: 
    def minimumRightShifts(self , nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # If already sorted, no shifts needed
        if nums == sorted_nums:
            return 0
        
        # Try all possible shifts from 1 to n-1
        for shift in range(1, n):
            # Right shift by 'shift' positions
            shifted = nums[-shift:] + nums[:-shift]
            if shifted == sorted_nums:
                return shift
        
        return -1
