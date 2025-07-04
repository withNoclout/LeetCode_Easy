class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        subst = {} 
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        idx = 0 
        for char in key:
            if char != ' ' and char not in subst:
                subst[char] = alphabet[idx]
                idx += 1
        
        # Decode message using substitution table
        result = ''
        for char in message:
            if char == ' ':
                result += ' '
            else:
                result += subst[char]
                
        return result
