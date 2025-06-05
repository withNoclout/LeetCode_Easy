class Solution(object):
    def largeGroupPositions(self, s):
        """
        Return intervals of large groups (3 or more consecutive same characters).
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0  # Start index of current group
        
        for i in range(len(s)):
            # If current character differs from next or end of string
            if i == len(s) - 1 or s[i] != s[i + 1]:
                # Check if group is large (3 or more characters)
                if i - start + 1 >= 3:
                    result.append([start, i])
                # Start new group at next index
                start = i + 1
        
        return result
