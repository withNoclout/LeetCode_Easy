class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result_freq = [0] * 26 

        for char in words[0] : 
            result_freq[ ord(char) - ord('a') ] += 1 


        for word in words[1 : ] : 
            curr_freq = [0] * 26
            for char in word : 
                curr_freq[ ord(char) - ord('a') ] += 1

            for i in range(26):
                result_freq[i] = min(result_freq[i], curr_freq[i])

        result = [] 
        for i in range(26): 
            result.extend([chr(i + ord('a'))] * result_freq[i])

        return result 
