class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

# Add a node at the head of the list.
    def add(self, data):
        self.size += 1
        if self.head:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            self.head = Node(data)

# Looks for a specific value in the list and deletes it.
    def delete(self, data):
        if self.head == None:
            print('List is empty')
            return

        prev = self.head
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                print('Deleted ' + str(data))
                return
            else:
                prev = current
                current = current.next
        print("Can't delete " + str(data) + " value not found")


# Checks if the value is in the list and returns a bool value accordingly.
    def find(self, data) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Returns the length of the list.
    def len(self) -> int:
        return self.size

# Prints all the values in the list in order.
    def list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
