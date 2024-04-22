class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next


if __name__ == "__main__":
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.print_list()
    l.delete(3)
    l.print_list()
    l.delete(1)
    l.print_list()
    l.delete(5)
    l.print_list()
    l.delete(2)
    l.print_list()
    l.delete(4)
    l.print_list()
