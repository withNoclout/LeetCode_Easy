class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        # Count frequencies in word1
        for char in word1:
            freq1[ord(char) - ord('a')] += 1
        
        # Count frequencies in word2
        for char in word2:
            freq2[ord(char) - ord('a')] += 1
        
        # Check if difference in frequencies for any letter exceeds 3
        for i in range(26):
            if abs(freq1[i] - freq2[i]) > 3:
                return False
        
        return True
