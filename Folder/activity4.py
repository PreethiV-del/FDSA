class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search_node(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index  
            current = current.next
            index += 1
        return -1  

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()


linked_list = LinkedList()
linked_list.append_node(10)
linked_list.append_node(20)
linked_list.append_node(30)

print("Linked List:")
linked_list.display_list()

search_value = 20
result = linked_list.search_node(search_value)
if result != -1:
    print(f"Node with value {search_value} found at index {result}")
else:
    print(f"Node with value {search_value} not found")

search_value = 40
result = linked_list.search_node(search_value)
if result != -1:
    print(f"Node with value {search_value} found at index {result}")
else:
    print(f"Node with value {search_value} not found")

linked_list.append_node(40)
print("Linked List after appending 40:")

linked_list.display_list()

