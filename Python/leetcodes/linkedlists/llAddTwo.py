#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
    prev1 = None
        cur1 = l1
        str1 = ""
        while cur1:
            str1 += str(cur1.val)
            temp1 = cur1.next
            cur1.next = prev1
            prev1 = cur1
            cur1 = temp1
        print(str1[::-1])
        prev2 = None
        cur2 = l2
        str2 = ""
        while cur2:
            str2 += str(cur2.val)
            temp2 = cur2.next
            cur2.next = prev2
            prev2 = cur2
            cur2 = temp2
        print(str2[::-1])
        total = int(str1[::-1]) + int(str2[::-1])
        totalstr = (str(total)[::-1])
        print('im a string' + totalstr)
        prev3 = None
        first = None
        for v in totalstr:
            cur3 = ListNode(v)
            if first is None:
                first = cur3
            if prev3 is not None:
                prev3.next = cur3
            prev3 = cur3
        return first