# Reverse a linked list:

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def add_to_front(self, node):
        self.head, node.next = node, self.head
        
    def add_to_end(self, node):
        head = self.head
        if head is None:
            # empty list
            self.head = node
        while head.next:
            # go to the end
            head = head.next
        head.next = node
        
    def print_list(self):
        head = self.head
        print('Linked List: ', end=' ')
        while head:
            print(head.data, end=' -> ')
            head = head.next
        print('NULL')
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        
mylist = LinkedList()
mylist.add_to_front(Node(1))
mylist.add_to_end(Node(2))
mylist.add_to_front(Node(3))
mylist.add_to_end(Node(4))
mylist.add_to_front(Node(5))
mylist.add_to_end(Node(6))
mylist.add_to_front(Node(7))
mylist.add_to_end(Node(8))
mylist.print_list()

print('Reversing...')
mylist.reverse()
mylist.print_list()
