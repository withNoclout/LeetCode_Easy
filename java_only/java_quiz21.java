class Solution{
    public ListNode mergTwoLists( ListNode  List1 , ListNode list2 ) {
        ListNode dummy = new ListNode( -1 )  ; 
        ListNode tail = dummy  ; 


        while ( list1 != null && list2 != null ) {
            if(list1.val <= list2.val ) {
                tail.next = list1  ; 
                list1 = list1.next ; 
            }else {
                tail.nect = list2  ; 
                list2 = list2.next ; 
            }
            tail = tail.next ; 
        }
        tail.next = ( lists1 != null ) ? list1 : list2 ; 
        return dummy.next   ; 
        
    }
}
