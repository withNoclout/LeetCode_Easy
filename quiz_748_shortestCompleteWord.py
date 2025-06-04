class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate_freq = [0] * 26 
        for char in licensePlate.lower() : 
            if char.isalpha() : 
                plate_freq[ ord( char) - ord('a' ) ] += 1 
        
        min_length = float('inf')
        result = '' 

        for word in words : 
            word_freq = [0] * 26 
            for char in word.lower() : 
                if char.isalpha() : 
                    word_freq[ ord(char ) - ord('a') ] += 1 

            is_valid  = True 
            for i in range(26 ) :
                if word_freq[i]  < plate_freq[i] : 
                    is_valid = False 
                    break 

            if is_valid and len(word) < min_length : 
                min_length = len(word ) 
                result = word 

        return result 
