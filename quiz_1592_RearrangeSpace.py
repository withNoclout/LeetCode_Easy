class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        total_spaces = text.count(' ')
        words = text.split()
        num_words = len(words)

        if num_words == 1 : 
            return words[0] + ' ' * total_spaces
        
        space_between = total_spaces // (num_words - 1) if num_words > 1 else 0
        extra_spaces = total_spaces % (num_words - 1) 

        return (' ' * space_between).join(words) + ' ' * extra_spaces
