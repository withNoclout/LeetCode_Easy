class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s) 
        left , right = 0 , len(s) - 1 

        while left < right : 
            if s[left ]  != s[right ] :
                if s[left ] < s[right ] : 
                    s[right  ] = s[left]  

                else : 
                    s[left ] = s[right ] 

            left += 1 
            right -= 1 

        return ''.join(s) 
