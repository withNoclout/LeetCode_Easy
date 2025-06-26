class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for char in s : 
            freq[char ] = freq.get(char , 0). + 1 


        freq_1 = set(freq.values())

        return len(freq_1 ) == 1 
