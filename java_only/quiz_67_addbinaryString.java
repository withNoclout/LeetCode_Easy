class Solution{
    public String addBianry( String a , String b ) {
        StringBuilder result = newStringBuilder() ; 


        int i = a.length() - 1 ; 
        int j = b.length()  -1 ; 
        int carry =  0 ; 


        while( i>= 0 || j >=  0  || carry > 0 ) {
            int bitA = ( i>= 0 ) ? a.charAt(i) - '0' : 0 ; 
            int bitB = ( i>= 0 ) ? b.charAt(j) - '0' : 0 ; 

            int sum = bitA + bitB + carry ;  
            result.append( sum % 2 ) ; 
            carry = sum / 2 ; 
            i-- ; 
            j-- ; 

        }
        return result.reverse().toString()  ;
    }
}
