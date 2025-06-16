class Solution:
    def stringMatching(self, words ): 
        # Sort words by length
        words.sort(key=len)
        result = set()  # Use set to avoid duplicates
        
        # Check shorter words against longer ones
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.add(words[i])
                    
        return list(result)
