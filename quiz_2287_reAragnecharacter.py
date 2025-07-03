class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        s_freq = {}
        for char in s : 
            s_freq[char] = s_freq.get(char , 0 ) + 1 

        target_freq = {}
        for char in target : 
            target_freq[char] = target_freq.get(char , 0 ) + 1 

        min_copies = float('inf')
        for char in target_freq :
            if char not in s_freq : 
                return 0 
            
            copies = s_freq[char] // target_freq[char ] 
            min_copies = min( min_copies , copies )

        return min_copies
