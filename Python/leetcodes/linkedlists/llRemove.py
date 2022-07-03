#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
    
#Dummy Node vs Pointer: Dummy node used when you need to refer to the original head node after progressing through the LL and making changes