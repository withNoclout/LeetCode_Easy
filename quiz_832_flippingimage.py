class Solution: 
    def flipAndInvertImage( self , image ) :
        n = len(image) 
        for i in range(n) : 
            for j in range(( n+1 ) // 2 ) :
                image[i][j] , image[i][ n-1-j] = 1 - image[i][n-1-j] , 1 - image[i][j] 

        return image  
