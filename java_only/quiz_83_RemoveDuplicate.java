class ListNode{
    int val ; 
    ListNode next  ; 
    ListNode()  { }
    ListNode(int val  ){
        this.val = val 
    }
    ListNode( int val , ListNode next  ) {
        this.val = val ; 
        this.next = next ; 

    }
}
class Solution{
    public ListNode deleteDuplicates( ListNode head ) {
        ListNode current = head ; 
        while ( current != null && current.next != null ) {
            System.out.println("Current node value : " + current.val ) ; 
            
            if(current.val == current.next.val ) { 
                System.out.println("Duplicate found"  + current.next.val + "Removeing it " )
                current.next  = current.next.next ; 

            }else { 
                current = current.next ; 
            }
        }
        return head ; 

    }

    public static void printList( ListNode  head ) {
        while( head != null ) {
            System.out.print(head.val )  ;  
            if ( head.next != null ) System.out.print( " >> ") ; 
            head = head.next  ; 

        }
        System.out.println( ) ;  

    }

    public static ListNode BuildLists( int[] values ) {
        if(values.length == 0 ) return null ; 
        ListNode head = new ListNode( value[0]  ) ; 
        ListNode current = head ; 
        for( int  i = 1 ; i < values.length  ; i++ ) {
            current.next = new ListNode(values[i] )  ;
            current = current.next ; 

        }
        return head ;  

    }
//test function 
    public static void main(String[] args ) {
        int[] input = {1 ,1 ,2, 3,4 } ; 
        ListNode head = buildList(input)  ; 

        System.out.print("Original List :" ) ; 
        printList(head ) ; 

        Solution sol = new Solution() ; 
        ListNode newHead = sol.deleteDuplicates(head ) ; 

        System.out.print("List after removing Duplicate : " )
        printList(newHead) ; 


        
    }
}
