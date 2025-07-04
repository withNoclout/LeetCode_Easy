class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        value_weight = {}

        for value , weight in items1 : 
            value_weight[value ] = value_weight.get(value , 0 ) + weight 

        for value , weight in items2 : 
            value_weight[value ] = value_weight.get(value , 0 ) + weight  

        result = [ [ value , weight ] for value , weight in value_weight.items()]

        result.sort( key= lambda x : x[0])

        return result 
