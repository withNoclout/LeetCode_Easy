class Solution : 
    def minMaxDifference(self , num ) :
        s = str(num ) 

        max_str = s 

        for c in s : 
            if c !=  '9'  :
                max_str = max_str.replace( c , '9' ) 
                break 

        min_str = s 
        for c in s :
            if c != '0' : 
                min_str = min_str.replace( c , '0' ) 
                break 

        max_val = int(max_str)
        min_val = int(min_str ) 

        return max_val - min_val 
