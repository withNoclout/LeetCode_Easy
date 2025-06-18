class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # missing = sum([ i for i in range(0 , k)])
        missing_count  = 0 
        current = 1 
        i = 0 
        while i < len(arr)  :
            if arr[i] == current : 
                i += 1 
                current += 1 
            else : 
                missing_count += 1 
                if missing_count == k :
                    return current
                current += 1 
        return current + ( k - missing_count ) - 1 
    
        
