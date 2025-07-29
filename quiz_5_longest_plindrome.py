class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter( left , right ) :
            while left >= 0 and right < len(s) and s[left] == s[right ] :
                left -= 1 
                right += 1 
            return s[left + 1 : right ] 
        
        longest = ''

        for i in range(len(s) ) :
            temp = expandAroundCenter(i, i)  # Odd length palindrome
            if len(temp) > len(longest):
                longest = temp

            temp = expandAroundCenter(i, i + 1)  # Even length palindrome
            if len(temp) > len(longest):
                longest = temp

        return longest 
