import ctypes
class Queue:
    def __init__(self): 
        self.cap = 10 # Assuem the fixed-size is 10
        self.size = 0
        self.readidx = 0
        self.writeidx = 0
        self.A = (self.cap * ctypes.py_object)() # create an array of size of the capacity

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.cap

    def enqueue(self, value):
        if not self.full():
            if self.writeidx == self.cap:
                self.writeidx = 0
            self.A[self.writeidx] = value
            self.writeidx += 1
            self.size += 1
        else:
            raise Exception("The queue is full!")

    def dequeue(self):
        if not self.empty():
            if self.readidx == self.cap:
                self.readidx = 0
            value = self.A[self.readidx]
            self.readidx += 1
            self.size -= 1
            if self.full():
                if self.writeidx == self.cap:
                    self.writeidx = 0
                else:
                    self.writeidx += 1
            return value
        else:
            raise Exception("The queue is empty!")

    def show(self):
        print "The size of the array: ", self.cap
        print "The size of the queue: ", self.size
        print "read index: ", self.readidx
        print "write index: ", self.writeidx
        startidx = self.readidx
        for i in range(self.size):
            if startidx == self.cap:
                startidx = 0
            print self.A[startidx]
            startidx += 1
q = Queue()
q.show()
        
q.enqueue(1) 
q.show()
q.enqueue(2) 
q.show()
q.enqueue(3) 
q.show()
q.enqueue(4) 
q.show()
q.enqueue(5) 
q.show()
q.enqueue(6) 
q.show()
q.enqueue(7) 
q.show()
q.enqueue(8) 
q.show()
q.enqueue(9) 
q.show()
q.enqueue(10) 
q.show()
q.dequeue()
q.show()
q.enqueue(11) 
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.enqueue(22)
q.show()
