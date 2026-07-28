class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# node1 = node(5)
# node2 = node(10)
# node3 = node(7)
# node4 = node(8)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# print(node1.val)
# print(node1.next.next.next.val)
# print(node2)

class SinglyLinkedList:
    def __init__(self):
      self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def Traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end = " ")
                current = current.next
            print()

    def insert_at(self,data,position):
        new_node = node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            if prev_node is not None:
                prev_node.next = new_node
                new_node.next = current

    def delete(self,data):
        temp = self.head
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next
                temp.next = None
            else:
                found = False
                prev_node = None
                while temp is not None:
                    if temp.data == data:
                        found = True
                        break
                    prev_node = temp
                    temp = temp.next

                if found:
                    prev_node.next = temp.next
                    return
                else:
                    print("Data not found in SLL")


sll = SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(7)
sll.append(8)
sll.append(9)

sll.Traverse()



    



   