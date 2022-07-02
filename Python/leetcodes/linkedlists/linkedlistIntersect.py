#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB #Once pointer a reaches the end, concatenate the two ll together
            if b:
                b = b.next
            else:
                b = headA #Once pointer b reaches the end, concatenate the two ll together
        return a