class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
    
class LinkedList: 
    def __init__(self): 
        self.head = None 
    
    def insert_at_beginning(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 
    
    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head: 
            self.head = new_node 
            return 
        last = self.head 
        while last.next: 
            last = last.next 
        last.next = new_node 
    
    def delete_node(self, data): 
        if not self.head: 
            return

        current = self.head
        if current and current.data == data: 
            self.head = current.next 
            current = None 
            return 
        
        prev = None 
        while current and current.data != data: 
            prev = current 
            current = current.next 
        
        if current is None: 
            return 
        
        prev.next = current.next 
        current = None 
    
    def traverse(self): 
        current = self.head 
        while current: 
            print(current.data, end=" -> " if current.next else "")
            current = current.next 
        print() 

linked_list = LinkedList() 

linked_list.insert_at_beginning(10) 
linked_list.insert_at_beginning(20) 
linked_list.insert_at_beginning(30)
print("Linked list after inserting 30, 20, 10 at the beginning:") 
linked_list.traverse() 

linked_list.insert_at_end(5) 
linked_list.insert_at_end(10)
linked_list.insert_at_end(15)
linked_list.insert_at_end(20)
print("\nLinked list after inserting 5, 10, 15, 20 at the end:") 
linked_list.traverse() 

linked_list.delete_node(15) 
print("\nLinked list after deleting node with data 15:") 
linked_list.traverse() 

print("\nTraversing the linked list:") 
linked_list.traverse()
