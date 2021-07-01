# Stack implementation using linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def traverse(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        print(current.data)
        

    def push(self, element):
        new_node = node(element)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else :
            self.head = new_node

    def pop(self):
        current = self.head
        if self.head:
            while current.next:
                pre = current
                current = current.next
            deleted = current
            pre.next = None
            return deleted
        else:
            return None

ll = LinkedList()
ll.push(11)
ll.push(12)
ll.push(13)
ll.push(14)
ll.push(15)
ll.push(16)
ll.push(17)
ll.push(18)
ll.traverse()
print("poped = ", ll.pop().data)
ll.traverse()











