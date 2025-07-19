class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m, n = len(mat), len(mat[0])
        
        # If k % n == 0, every row returns to its original state
        k = k % n
        if k == 0:
            return True
        
        # If n == 1, single-element rows don't change with shifts
        if n == 1:
            return True
        
        # Check each row
        for i in range(m):
            original_row = mat[i]
            # Check if all elements in the row are the same
            if all(x == original_row[0] for x in original_row):
                continue  # Identical elements mean the row stays the same after any shift
            
            # Compute effective shift
            shift = k if i % 2 == 0 else -k  # Even: left shift; Odd: right shift
            shift = shift % n  # Normalize shift
            
            # Check if shifted row matches original
            for j in range(n):
                # Index after shift: (j + shift) % n
                if original_row[j] != original_row[(j + shift) % n]:
                    return False
        
        return True
