class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Head
    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    # 2. Insert at Tail
    def insert_at_Tail(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # 3. Insert at Position
    def insert_at_position(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current and count < position-1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node