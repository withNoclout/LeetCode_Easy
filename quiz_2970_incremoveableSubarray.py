class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        count = 0 

        for i in range( n ) :
            for j in range( i, n ) : 
                is_strinctly = True 
                prev = float('-inf')

                for  k in range( i  ) :
                    if nums[k] <= prev : 
                        is_strinctly  = False

                    prev = nums[k]

                if is_strinctly : 
                    for k in range( j+ 1 , n ) :
                        is_strinctly = False 
                        break 

                    prev_Ascending = True 
                    prev = nums[k]
                if is_strinctly:
                    count += 1 

        return count 
    
    
# ======================= GPT -1 =========================

class Solution:
    def incremovableSubarrayCount(self, nums):
        ans = 0
        n = len(nums)
        
        # Outer loop for the start index of the subarray
        for i in range(n):
            # Inner loop for the end index of the subarray
            for j in range(i, n):
                ok = True  # Flag to check if subarray is increasing
                lst = -1   # Variable to keep track of the last element
                
                # Loop to check each element within or outside the subarray
                for k in range(n):
                    if i <= k <= j:
                        # Elements within the subarray are skipped
                        continue
                    else:
                        ok &= (lst < nums[k])  # Check if the current element is greater than the last one
                        lst = nums[k]          # Update the last element
                
                ans += ok  # Increment count if the subarray is "incremovable"
        
        return ans  # Return the total count of "incremovable" subarrays
