class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
# def makeGood(s: str) -> str:
        result = ""
        for char in s:
            if result and (
                (char.isupper() and result[-1] == char.lower()) or
                (char.islower() and result[-1] == char.upper())
            ):
                result = result[:-1]  # Remove last character
            else:
                result += char
        return result
