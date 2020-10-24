class Node:
    def __init__(self, _d, _n=None):
        self.data = _d
        self.next = _n

    def get_next(self):
        return self.next
    
    def set_next(self, _n):
        self.next = _n
        
class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, _d):
        new_node = Node(_d, self.root)
        self.root = new_node
        self.size += 1
        return True
    
    def print(self):
        curr = self.root
        print('Linked list:', end='\t')
        while curr:
            print(curr.data, '->', end=' ')
            curr = curr.next
        print('NULL\n')
            
    def delete(self, _d):
        """Delete a node. """
        curr = self.root
        prev = None
        while curr:
            if curr.data == _d:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.root = curr
                self.size -= 1
                print('Element {} deleted.'.format(_d))
                return
            prev = curr
            curr = curr.next
        print('Element {} not found'.format(_d))
        
    def append_list(self, other):
        """Append another linked list. """
        curr = self.root
        while curr.next:
            curr = curr.next
        curr.next = other.root
        
    def reverse(self):
        """Reverse a linked list. """
        newlist = LinkedList()
        curr = self.root
        while curr:
            newlist.add(curr.data)
            curr = curr.next
        self.root = newlist.root
        
    def sort(self, ascending=True):
        """Sort list in-place using bubble-sort. """
        node1 = self.root
        while node1.next:
            node2 = node1.next
            while node2:
                if ascending:
                    if node2.data < node1.data:
                        node1.data, node2.data = node2.data, node1.data
                else:
                    if node2.data > node1.data:
                        node1.data, node2.data = node2.data, node1.data
                node2 = node2.next
            node1 = node1.next
            
# Test cases:
mylist = LinkedList()
mylist.add(1)
mylist.add(4)
mylist.add(9)
mylist.add(25)
mylist.print()

mylist.delete(8)
mylist.delete(9)
mylist.print()

other = LinkedList()
other.add(100)
other.add(200)
other.add(300)
other.print()

mylist.append_list(other)
mylist.print()

mylist.reverse()
mylist.print()

mylist.add(8)
mylist.add(23)
mylist.add(4)
mylist.add(2)
mylist.print()

mylist.sort()
mylist.print()
