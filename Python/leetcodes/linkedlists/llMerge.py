#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy points to the initial/head node
        cur = dummy # cur progresses through the linked list for the purposes of the problem so cant be the variable returned
        
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next