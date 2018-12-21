"""
This is a Double Linked List implementation in Python
with the usage of sentinel node
"""

class DList:
    
    def __init__(self):
        self.size = 0
        self.sentN = DNode("sent", None, None)
        self.sentN.preN = self.sentN
        self.sentN.nextN = self.sentN

    def size(self):
        return self.size

    def empty(self):
        return (self.sentN.preN == self.sentN.nextN and self.sentN.preN == self.sentN)

    def value_at(self, index):
        if index >= self.size:
            raise Exception("The index is out of boundary")
        current = self.sentN.nextN
        count = 1
        while(count <= index):
            current = current.nextN 
            count += 1
        return current.data

    def push_front(self, value):
        newNode = DNode(value, self.sentN, self.sentN.nextN)
        self.sentN.nextN.preN = newNode        
        self.sentN.nextN = newNode
        self.size += 1
           
    def pop_front(self):
        if not self.empty():
            value = self.sentN.nextN.data
            self.sentN.nextN = self.sentN.nextN.nextN
            self.sentN.nextN.preN = self.sentN
            self.size -= 1
            return value 
        else:
            raise Exception("The list is empty!")

    def push_back(self, value):
        newNode = DNode(value, self.sentN.preN, self.sentN)
        self.sentN.preN.nextN = newNode
        self.sentN.preN = newNode
        self.size += 1

    def pop_back(self):
        if not self.empty():
            value = self.sentN.preN.data
            self.sentN.preN = self.sentN.preN.preN
            self.sentN.preN.nextN = self.sentN
            self.size -= 1
            return value
        else:
            raise Exception("The list is empty!")

    def front(self):
        if not self.empty():
            return self.sentN.nextN.data
        else:
            raise Exception("The list is empty")

    def back(self):
        if not self.empty():
            return self.sentN.preN.data
        else:   
            raise Exception("The list is empty")

    def insert(self, index, value):
        if index >= self.size:
            raise Exception("The index is out of boundary")
        current = self.sentN.nextN
        count = 1
        while(count <= index):
            current = current.nextN 
            count += 1
        newNode = DNode(value, current.preN, current)
        current.preN.nextN = newNode
        current.preN = newNode
        self.size += 1

    def erase(self, index):
        if index >= self.size:
            raise Exception("The index is out of boundary")
        current = self.sentN.nextN
        count = 1
        while(count <= index):
            current = current.nextN 
            count += 1
        current.nextN.preN = current.preN
        current.preN.nextN = current.nextN
        self.size -= 1

    def value_n_from_end(self, n):
        if n >= self.size:
            raise Exception("The index is out of boundary")
        current = self.sentN.preN
        count = 1
        while(count < n):
            current = current.preN 
            count += 1
        return current.data

    def reverse(self):
        current = self.sentN
        count = 0
        while(count <= self.size):
            pre = current.preN
            current.preN = current.nextN
            current.nextN = pre
            current = current.preN
            count += 1
            

    def remove_value(self, value):
        current = self.sentN
        count = 0
        while(count <= self.size):
            if current.data == value:
                current.preN.nextN = current.nextN
                current.nextN.preN = current.preN
                break
            current = current.nextN 
            count += 1
        self.size -= 1
    
    def show(self):
        print "size: ", dlist.size
        print "empty?: ", dlist.empty()
        print "List is: "
        current = self.sentN.nextN
        for i in range(self.size):
            print "current:", current.data
            print "pre node: ", current.preN.data
            print "next node: ", current.nextN.data
            current = current.nextN

class DNode:
    """
    This class defines a node
    with pointers to the previous node
    and the next node
    """
    def __init__(self, data, preN, nextN):
        self.data = data
        self.preN = preN
        self.nextN = nextN


dlist = DList()
dlist.show()

dlist.push_front(1)
dlist.push_front(2)
dlist.push_front(3)
dlist.show()

dlist.push_back(4)
dlist.push_back(5)
dlist.push_back(6)
dlist.show()

print "value at index 3:", dlist.value_at(3)
print "value at index 0:", dlist.value_at(0)

print "pop front: ", dlist.pop_front()
dlist.show()
print "pop front: ", dlist.pop_front()
dlist.show()

print "pop back: ", dlist.pop_back()
dlist.show()
print "pop back: ", dlist.pop_back()
dlist.show()
print "pop back: ", dlist.pop_back()
dlist.show()
print "pop back: ", dlist.pop_back()
dlist.show()

dlist.push_back(1)
dlist.push_back(2)
dlist.push_back(3)
dlist.push_back(4)
dlist.push_back(5)
dlist.push_back(6)
print "front value: ", dlist.front()
print "back value: ", dlist.back()
dlist.show()

print "inserting 22 at index 3"
dlist.insert(3,22)
dlist.show()

print "erasing at index 5"
dlist.erase(5)
dlist.show()

print "nth value from the end: ", dlist.value_n_from_end(3)
dlist.show()

print "reverse the list: "
dlist.reverse()
dlist.show()

print "removing 3"
dlist.remove_value(3)
dlist.show()
