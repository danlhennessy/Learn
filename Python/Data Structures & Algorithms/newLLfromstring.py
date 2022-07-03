class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

totalstr = ["Stringtest"]


prev = None
first = None
for v in totalstr:
    cur = ListNode(v)
    if first is None:
        first = cur
    if prev is not None:
        prev.next = cur
    prev = cur
    
# first = linked list

cur1 = first
while cur1:
    print(cur1.val)
    cur1 = cur1.next