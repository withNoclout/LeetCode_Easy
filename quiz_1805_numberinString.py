class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = ''.join( ' ' if not c.isdigit() else c for c in word )

        numbers = { str(int(num)) for num in word.split(  ) if num }

        return len(numbers)
