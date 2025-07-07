class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char_sets = [ frozenset(word) for word in words ] 

        count = 0 
        freq = {}
        for char_set in char_sets : 
            if char_set in freq :
                count += freq[char_set ]
                freq[char_set ] += 1 
            else : 
                freq[char_set ] = 1 


        return count
