class Solution(object):
    def removeDuplicates(self, s):
        """
        Remove all adjacent duplicates from string s until no more can be removed.
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
