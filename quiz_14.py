class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Start with the first string as the prefix
        prefix = [] 
        
        for word in zip(*strs): 
            # Check if all characters in the current position are the same
            if len(set(word)) == 1:
                prefix.append(word[0])
            else:
                break   
        return ''.join(prefix)
    

