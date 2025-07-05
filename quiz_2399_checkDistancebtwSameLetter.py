class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        positions = {}
        for i , char in enumerate(s ) :
            if char in positions : 
                positions[char].append(i)

            else: 
                positions[char] = [i]

        for char , pos in positions.items() : 
            letter_idx = ord(char ) - ord('a')

            if pos[1] - pos[0] - 1 != distance[letter_idx ] 
            return False 
        
        return True 
