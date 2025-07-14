class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0 
        seen = set()

        for word in words : 
            if word[::-1] in seen : 
                count += 1 
            seen.add(word ) 

        return count  
