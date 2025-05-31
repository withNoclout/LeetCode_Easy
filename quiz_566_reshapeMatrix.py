class Solution: 
    def matrixResharp( self , mat , r , c ) :
        m = len(mat )
        n = len( mat[0])

        if m *n != r * c : 
            return mat 
        
        flat = [] 
        for row in mat : 
            for val in row : 
                flat.append(val)


        result = [] 
        for i in range(r ) :
            row = [] 
            for j in range( c) :
                row.append( flat[ i * c + j ])
            result.append(row ) 


        return result
