class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        target = (sumA - sumB) // 2
        
        setB = set(bobSizes)
        
        for a in aliceSizes:
            if (a - target) in setB:
                return [a, a - target]
        
        return []   
