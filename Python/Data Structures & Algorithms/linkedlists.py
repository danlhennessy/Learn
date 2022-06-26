#Linked lists contain nodes. Each node has 2 parts: Data and a pointer to the next node. The first node is the head node


class node(object):
    def __init__ (self, data=None):
        self.data=data
        self.next=None
        
class linkedlist(object):
    def __init__(self):
        self.head = node()
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    def get(self, index):
        if index >= self.length():
            print("ERROR: out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while cur_idx != index:
            cur_node = cur_node.next
            cur_idx += 1
        return cur_node.next.data
    def erase(self, index):
        if index >= self.length():
            print("ERROR: out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

my_list = linkedlist()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.erase(2)
my_list.display()