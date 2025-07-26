class Solution:
    def hasMatch(self, s , p ) : 
        x = p.find("*")
        b = p[:x]
        e = p[x + 1:]
        i = s.find(b)
        j = s.rfind(e)
        return i != -1 and j != -1 and i + len(b) <= j
