class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import re 
        pattern = re.compile(needle)
        match = pattern.search(haystack)
        if match:
            return match.start()
        else:
            return -1
        
