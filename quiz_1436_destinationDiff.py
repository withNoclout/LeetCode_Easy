class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set(cityA for cityA , _ in paths) 
        destinations = set( cityB for _ , cityB in paths ) 
        return ( destinations - sources ).pop()
