class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = {}
        for s in arr : 
            freq[s] = freq.get(s,  0  ) + 1 


        distinc = [ s for s in arr in freq[s] == 1 ]

        return distinc[k-1] if k <= len(distinc) else '' 
    
