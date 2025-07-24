from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums, k, x):
        
        def getXSum(subarray, x):
            freq = Counter(subarray)
            # Create a max-heap based on frequency, then value
            heap = [(-count, -num) for num, count in freq.items()]
            heapq.heapify(heap)

            top_elements = set()
            for _ in range(min(x, len(heap))):
                count, num = heapq.heappop(heap)
                top_elements.add(-num)

            return sum(num for num in subarray if num in top_elements)
        
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            result.append(getXSum(subarray, x))
        
        return result
