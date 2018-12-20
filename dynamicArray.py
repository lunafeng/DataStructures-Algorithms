import ctypes

class DynamicArray(object):
    """
    This is an implementation of dynamic array in Python
    using ctype module as raw array
    """
    def __init__(self):
        self.size = 0
        self.capacity = 1 # start with 1, use power of 2 later on to increase
        self.A = self.make_array(self.capacity)
    
    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def is_empty(self):
        return (self.size == 0)

    def at(self, index):
        if index > self.size - 1 or index < 0:
            raise Exception('The index is out of boundary')
        return self.A[index]

    def push(self, item):
        self._resize()
        self.A[self.size] = item
        self.size += 1

    def insert(self, index, item):
        self._resize()
        for i in range(self.size - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]
        self.A[index] = item
        self.size += 1

    def prepend(self, item):
        self._resize()
        for i in range(self.size - 1, -1, -1):
            self.A[i + 1] = self.A[i]
        self.A[0] = item
        self.size += 1

    def pop(self):
        popV = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize()
        return popV
    
    def delete(self, index):
        for i in range(index, self.size - index + 1):
            self.A[i] = self.A[i + 1]
        self.size -= 1
        self._resize()

    def remove(self, item):
        for i in range(self.size):
            if self.A[i] == item:
                for j in range(i, self.size -1):
                    self.A[j] = self.A[j+1]
                self.size -= 1
        self._resize()

    def find(self, item):
        for i in range(self.size):
            if self.A[i] == item:
                return i
        return -1
            

    def _resize(self):
        if self.size == self.capacity:
            print "resizing up"
            self.capacity = 2 * self.capacity
        if self.size == int(0.25 * self.capacity) and self.size != 0:
            print "resizing down"
            self.capacity = int(0.5 * self.capacity)
        newA = self.make_array(self.capacity)
        # copy elements to the new array
        if self.size != 0:
            for i in range(self.size):
                newA[i] = self.A[i]
            self.A = newA
    
    def make_array(self, cap):
        return (cap * ctypes.py_object)() # return an array of size of the capacity

    def showStats(self):
        print "Capacity is: ", self.capacity
        print "Size is: ", self.size
        print "Array is:" 
        if self.size > 0:
            for i in range(self.size):
                print self.A[i]
        else:
            print "NULL"

da = DynamicArray()
# Test push method
da.showStats()
da.push(1)
da.showStats()
da.push(2)
da.showStats()
da.push(3)
da.showStats()
da.push(4)
da.showStats()
da.push(5)
da.showStats()
da.push(6)
da.showStats()
da.push(7)
da.showStats()

# Test at method
print "Index at 4 is:"
print da.at(4)

#print "Index at 8 is:"
#print da.at(8)

# Test insert method
da.insert(2, 22)
da.showStats()
da.insert(5,55)
da.showStats()
da.insert(0, 9)
da.showStats()

# Test prepend method
da.prepend(11)
da.showStats()

# Test pop method
print "Pop: ", da.pop()
da.showStats()

# Test delete method
da.delete(2)
da.showStats()

# Test remove method
da.insert(5,11)
da.showStats()
da.remove(11)
da.showStats()

# Test find method
print "find index: ", da.find(22)
