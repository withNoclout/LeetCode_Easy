class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()

        for word in words : 
            morse_word = ''
            for chat in word : 
                morse_word += morse[ ord(char) - ord('a')]
            transformations.add( morse_word)

        return len(transformations)
