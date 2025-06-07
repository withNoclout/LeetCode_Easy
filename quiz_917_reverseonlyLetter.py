class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        Reverse only English letters in the string, keeping other characters in place.
        :type s: str
        :rtype: str
        """
        # Convert string to list for in-place modification
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until an English letter is found
            while left < right and not s_list[left].isalpha():
                left += 1
            # Move right pointer until an English letter is found
            while left < right and not s_list[right].isalpha():
                right -= 1
            # Swap letters
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        # Convert back to string
        return ''.join(s_list)
