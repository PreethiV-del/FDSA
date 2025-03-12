class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return  
            current = current.next

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> " if current.prev else "")
            current = current.prev
        print()

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(20)
dll.insert_at_end(40)

print("Original list:")
dll.traverse_forward()

dll.delete_node(20)
print("List after deleting the first 20:")
dll.traverse_forward()

print("Traversing backward:")
dll.traverse_backward()