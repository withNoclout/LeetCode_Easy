class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        Perform flood fill on the image starting from (sr, sc) with new color.
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # If starting pixel is already the target color, return image
        if image[sr][sc] == color:
            return image
        
        # Store original color to replace
        old_color = image[sr][sc]
        
        def dfs(r, c):
            # Check if current position is valid and has old_color
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != old_color):
                return
            
            # Change current pixel to new color
            image[r][c] = color
            
            # Recursively process 4-directional neighbors
            dfs(r-1, c)  # Up
            dfs(r+1, c)  # Down
            dfs(r, c-1)  # Left
            dfs(r, c+1)  # Right
        
        # Start DFS from (sr, sc)
        dfs(sr, sc)
        return image
