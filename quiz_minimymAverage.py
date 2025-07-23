class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        average = [] 
        nums.sort()
        left , right = 0 , len(nums) - 1 

        while left < right : 
            avg = ( nums[left] + nums[right ] ) / 2 
            average.append(avg)

            left += 1 
            right -= 1 


        return min(averange)
