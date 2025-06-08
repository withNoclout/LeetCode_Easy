class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums ) 
        # result  = [0] * n 
        # left , right = 0 , n - 1 

        # pos = n - 1 

        # while left <= right : 
        #     left_sqaure = nums[left ] * nums[left ] 
        #     right_square = nums[right ]  * nums[right ] 

        #     if left_sqaure > right_square : 
        #         result[pos] = left_sqaure 
        #         left += 1
        #     else : 
        #         result[pos ] = right_square
        #         right -= 1  
        #     pos -= 1

        # return result
     
        result = [] 
        for num in nums :
            result.append( num * num )

        return sorted(result)
