class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs or not strs[0] : 
            return 0 
        
        delete_count = 0
        cols = len(strs[0])

        for col in range(cols ) : 
            for row in range( 1,  len(strs) ) :
                if strs[row][col] < strs[row-1 ][col] :
                    delete_count += 1 
                    break 

        return delete_count
