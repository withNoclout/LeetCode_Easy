class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def process_string(string):
            stack = []
            for char in string : 
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return process_string(s) == process_string(t)
