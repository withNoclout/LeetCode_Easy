class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_freq = [0] * 26 
        for c in chars : 
            char_freq[ ord(c) - ord( 'a' ) ] += 1 

        total_length = 0 

        for word in words : 
            curr_freq = char_freq[ : ] 
            can_form = True 

            for c in word : 
                idx = ord(c) - ord( 'a' )
                if curr_freq[idx ] == 0 : 
                    can_form = False 
                    break 
                curr_freq[idx] -= 1 

            if can_form : 
                total_length += len( word ) 

        return total_length
