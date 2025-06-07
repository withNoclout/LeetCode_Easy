class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        Check if deck can be partitioned into groups of size x > 1 with same integers.
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        from functools import reduce
        
        # Custom GCD function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Count frequency of each integer
        freq = Counter(deck)
        frequencies = list(freq.values())
        
        # Handle edge cases
        if not frequencies:
            return False
        if len(frequencies) == 1:
            return frequencies[0] >= 2
        
        # Compute GCD for multiple frequencies
        gcd_val = reduce(gcd, frequencies)
        return gcd_val >= 2
