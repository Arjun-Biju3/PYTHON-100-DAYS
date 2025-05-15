# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not present
        if current is None:
            return

        prev.next = current.next
        current = None


# Create list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()   # Output: 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()   # Output: 10 -> 30 -> None
