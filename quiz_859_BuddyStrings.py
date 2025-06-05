class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        
        if s == goal : 
            return len(set(s)) < len(s) 
        
        diffs = []
        for i in range()(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)

        return len(diffs) == 2 and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]
