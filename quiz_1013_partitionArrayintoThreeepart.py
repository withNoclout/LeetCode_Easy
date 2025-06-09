class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        current_sum = 0
        parts=  0 
        n = len(arr)

        for i in range(n)  :
            current_sum +=  arr[i]

            if current_sum == target:
                parts += 1
                current_sum = 0

                if parts == 2 and i < n - 1:
                    return True 
                
                if parts == 1 and i >= n -2 : 
                    return False 
                
        return parts == 3 
