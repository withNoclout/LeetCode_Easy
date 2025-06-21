class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        piece_map = { p[0] : p for p in pieces } 

        i = 0 
        while i < len(arr) : 
            if arr[i] not in piece_map : 
                return False 
            
            piece = piece_map[arr[i]]
            for j in range( len( piece ) ) : 
                if i + j >= len(arr) or arr[i+j ] != piece[j]  : 
                    return False 
                
            i += len(piece)

        return True 
