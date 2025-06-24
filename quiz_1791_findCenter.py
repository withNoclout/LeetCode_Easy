class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a ,b = edges[0]
        c,d = edges[1]

        return a if a == c or a == d else b 
