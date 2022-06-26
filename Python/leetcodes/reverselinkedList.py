#Given the head of a singly linked list, reverse the list, and return the reversed list.


def reverseListIter(head):
    rev = None
    while head: 
        head.next, rev, head = rev, head, head.next #Changes the pointer from every -> to <- in linked list so that it will point backwards
    return rev # Returns reversed list