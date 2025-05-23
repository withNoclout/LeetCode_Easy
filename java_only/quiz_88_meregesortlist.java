import java.util.Arrays ; 

class Solution{
    public Void merge( int[] nums1  , int m , int[] nums2 , int n ) {
        int i = m -1  ; 
        int j = n -1 ;  
        int k = m + n  -1 ; //pointer for the final position in nums1 

        System.out.println('Starting merge :'  ) ; 
        System.out.println("Initial nums1 : " + Arrays.toString(nums1) ) ; 
        System.out.println("Initial nums2 : " + Arrays.toString(nums2) ) ;

        while ( i >= 0 && j >= 0 ) {
            System.out.println("Comparing nums1[" + i + "] = " + nums1[i] + " and nums2[" + j + "] = " + nums2[j]);
            if(nums1[i]  >  nums2[j] ) {
                nums1[k--] = nums1[i-- ]  ; 

            }else {
                nums1[k-- ] = nums2[j-- ] ; 

            }
            System.out.println("After remaining nums2 : " + Arrays.toString(nums1)) ; 
        }

        while( j >=0  ) {
            nums1[k-- ]  = nums2[j --]
            System.out.println("Copying remaining nums2: " + Arrays.toString(nums1));
        }
        System.out.println("Final merged array: " + Arrays.toString(nums1));

    }


    public static void(String[] args  ){
        Solution sol = new Solution() ; 
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        int m = 3, n = 3;
        
        sol.merge( nums1 , m , nums2 , n )  ; 
    
    }
}
