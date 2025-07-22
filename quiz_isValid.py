class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
                
        has_vowel = False
        has_consonant = False
        
        for char in word:
            if not (char.isalnum()):
                return False
            if char.lower() in 'aeiou':
                has_vowel = True
            elif char.isalpha():
                has_consonant = True
                
        return has_vowel and has_consonant
