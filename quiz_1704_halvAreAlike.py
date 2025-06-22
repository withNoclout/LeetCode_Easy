class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        n = len(s) // 2
        a, b = s[:n], s[n:]

        count_a = sum(1 for char in a if char in vowels)
        count_b = sum(1 for char in b if char in vowels)

        return count_a == count_b
