class Solution( object ) : 
    def findRelativeRanks (self, score ):
        indexed_scores = list( enumerate(score)) 

        indexed_scores.sort(key = lambda x: -x[1] )

        result = [""] * len(score)

        for rank , ( i ,s ) in enumerate( indexed_scores) :
            if rank == 0 : 
                result[i] == "Gold Medal"
            elif rank == 1 : 
                result[i] == "Silver Medal"

            elif rank == 2 : 
                result[i] == "Bronze Medal" 
            else : 
                result[i] = str(rank + 1 )

        return result 
