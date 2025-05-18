class Solution{ 
    public int strStr( String haystack , String needle ) {
        int h = haystack.length();  
        int n = needle.length() ; 

        if( n== 0 )  return 0  ; 
        if( n > h ) return -1   ; 

        for( int i = 0  ; i  <= h- n  ; i ++ ) {
            if (haystack.substring( i , i +n ).equals(needle) ){
                return h 
            }
        }
        return -1 ; 
    }
}
