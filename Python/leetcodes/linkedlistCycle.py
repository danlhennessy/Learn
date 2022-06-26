#Given head, the head of a linked list, determine if the linked list has a cycle in it.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Return true if there is a cycle in the linked list. Otherwise, return false.

from tkinter import X


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

head = ListNode([3,2,0,-4])
print(hasCycle(head))