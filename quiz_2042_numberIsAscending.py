class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tokens = s.split()

        numbers = [int(token) for token in tokens if token.isdigit()]

        for i in range( 1, len(numbers) ):
            if numbers[i] <= numbers[i-1 ] : 
                return False 
            
        return True 
