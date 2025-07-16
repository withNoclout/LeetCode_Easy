class Solution :
    def canBeEqual( self, s1, s2):
        # Check if characters at indices 0 and 2 can match after possible swap
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        
        # Check if characters at indices 1 and 3 can match after possible swap
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
        
        return True
