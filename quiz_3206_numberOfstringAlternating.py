class Solution : 
    def numberOfAlternatingGroups(self , colors) : 
        n = len(colors)
        count = 0
        
        # Since it's a circle, check each position including wrap-around
        for i in range(n):
            # Check if colors[i], colors[(i+1)%n], colors[(i+2)%n] form an alternating group
            if (colors[i] != colors[(i + 1) % n] and 
                colors[(i + 1) % n] != colors[(i + 2) % n]):
                count += 1
                
        return count
