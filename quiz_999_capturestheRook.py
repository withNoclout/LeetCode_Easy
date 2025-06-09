class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rook_row , rook_col = 0 ,  0
        for i in range(8)  :
            for j in range(8) : 
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break   

        captures = 0 

        for i in range( rook_row -1 , -1 , -1 ) :
            if board[i][rook_col] == 'B':
                break
            elif board[i][rook_col] == 'p':
                captures += 1
                break

        for i in range( rook_row + 1 , 8 ) :
            if board[i][rook_col] == 'B':
                break
            elif board[i][rook_col] == 'p':
                captures += 1
                break   

        for j in range( rook_col -1 , -1 , -1 ) :
            if board[rook_row][j] == 'B':
                break
            elif board[rook_row][j] == 'p':
                captures += 1
                break   

        for j in range( rook_col +1 , 8 ):
            if board[rook_row][j] == 'B':
                break
            elif board[rook_row][j] == 'p':
                captures += 1
                break   

        return captures 
    
