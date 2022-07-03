#Given the head of a singly linked list, reverse the list, and return the reversed list.


def reverseListIter(head):
    rev = None
    while head: 
        head.next, rev, head = rev, head, head.next #Changes the pointer from every -> to <- in linked list so that it will point backwards
    return rev # Returns reversed list

def reverseList2(head):
    prev = None # Starts as None, as in the end of a linked list
    cur = head 
    while cur:
        temp = cur.next # Stores Node in -> pointer direction as a temp variable
        cur.next = prev # Changes the next pointer to target prev node
        prev = cur # Moves prev forwards one step to cur node
        cur = temp # Moves cur forwards one step to temp forward node
    return prev # Prev ends up being the head of the reversed linked list when cur reaches the end and becomes None