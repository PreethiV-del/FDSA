class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self,data):
        current = self.head
        while current is not None:
            if current.data == data:

                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                return
            current = current.next
        print("Node with data", data, "not found in the list.")

#Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(30)
    dll.insert_at_beginning(50)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(10)

    print("Before deletion:")
    current = dll.head
    while current is not None:
        print(current.data, end="->")
        current = current.next

    dll.delete_node(20)

    print("\nAfter deletion:")
    current = dll.head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    


            

            



