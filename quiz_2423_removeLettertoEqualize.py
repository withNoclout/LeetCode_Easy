class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # Count frequency of each letter
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        
        # Get set of frequencies
        values = list(freq.values())
        
        # Try removing one occurrence of each letter
        for i in range(len(values)):
            # Decrease frequency by 1
            values[i] -= 1
            
            # Remove 0 frequencies
            temp = [x for x in values if x > 0]
            
            # Check if all remaining frequencies are equal
            if len(set(temp)) == 1:
                return True
                
            # Restore frequency
            values[i] += 1
        
        return False
