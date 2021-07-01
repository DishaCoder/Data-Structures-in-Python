class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        print("Length of LL = ", total)

    def traverse(self):
        current = self.head
        while current.next != None:
            current = current.next
            print(current.data)

    def get_position(self, position):
        current = self.head
        cur_pos = 1
        while cur_pos != position+1:
            current = current.next
            cur_pos += 1
        #print("Data at node", position, " = ", current.data)

    def insert(self, value, position): # 1->2->15->"disha"->6666.33
        new_node = node(value)
        current = self.head
        cur_pos = 1
        while cur_pos != position+1:
            pre = current
            current = current.next
            cur_pos += 1
        pre.next = new_node
        new_node.next = current

    def delete(self, value):
        current = self.head
        while current.data != value:
            pre = current
            current = current.next
        pre.next = current.next
        
        



l = linked_list()
l.append(1)
l.append(2)
l.append(15)
l.append("disha")
l.append(6666.33)
l.insert(85,3)
l.delete(15)
l.length()
l.traverse()
print("get position : ", l.get_position(4).data)







