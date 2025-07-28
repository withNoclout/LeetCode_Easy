class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter 

        freq = Counter(s) 

        if len(freq) <  k :
            return 0 
        

        freqs = sorted( freq.values() , reverse=True) 
        return sum(freq[k : ])
