# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        decimal = 0 
        current = head 

        while current : 
            decimal = decimal * 2 + current.val
            current = current.next 

        return decimal 
