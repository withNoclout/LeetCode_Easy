class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for word in words : 
            if len(word) <= len(s)  and s[:len(word)] == word : 
                count += 1 
        return count 
