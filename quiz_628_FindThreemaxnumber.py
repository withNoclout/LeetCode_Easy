class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        
        # กรณี 1: สามตัวท้ายสุด
        product1 = nums[-1] * nums[-2] * nums[-3]
        
        # กรณี 2: สองตัวลบสุด + ตัวบวกสุด
        product2 = nums[0] * nums[1] * nums[-1]
        
        return max(product1, product2)
