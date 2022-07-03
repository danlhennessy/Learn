#In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

#For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
#The twin sum is defined as the sum of a node and its twin.

#Given the head of a linked list with even length, return the maximum twin sum of the linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur1 = head
        cur2 = prev
        sum = 0
        while cur2:
            print(cur1.val + cur2.val)
            if cur1.val + cur2.val > sum:
                sum = cur1.val + cur2.val
            cur2 = cur2.next
            cur1 = cur1.next
        print(sum)

