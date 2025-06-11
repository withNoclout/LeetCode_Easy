class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        zeros = arr.count(0)
        n = len(arr)

        i = n - 1 
        j = n + zeros - 1 

        while  i >= 0 and j >=  0 : 
            if arr[i] == 0 : 
                if j < n : 
                    arr[j] =  0 
                j -= 1 
                if j < n : 
                    arr[j] = 0 
            else : 
                if j < n : 
                    arr[j] = arr[i] 

            i -= 1 
            j-= 1 
            
