#Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

#Return the decimal value of the number in the linked list.

def getDecimalValue(head):
    string = ""
    while head:
        string += str(head.val)
        head = head.next
    return int(string, 2)

#Alternate:

def getDecimalValue(self, head: ListNode) -> int:
    answer = 0
    while head: 
        answer = 2*answer + head.val 
        head = head.next 
    return answer 