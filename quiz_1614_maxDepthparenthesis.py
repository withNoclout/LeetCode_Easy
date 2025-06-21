class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = max_depth = 0 
        for char in s : 
            if char == '(' :
                depth += 1 
                max_depth = max(max_depth, depth)
            elif char == ')' :
                depth -= 1
        return max_depth if depth == 0 else 0
