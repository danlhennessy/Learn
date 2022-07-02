#Given the head of a singly linked list, return true if it is a palindrome.

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string1 = ""
        while head:
            string1 += str(head.val)
            head = head.next
        if string1 == string1[::-1]:
            return True
        else:
            return False