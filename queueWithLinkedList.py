class SNode:
    def __init__(self, data, nextN):
        self.data = data
        self.nextN = nextN

class Queue:
    def __init__(self):
        self.size = 0
        self.tail = SNode(None, None)
        self.head = SNode(None, self.tail)

    def empty(self):
        return self.head.nextN == self.tail

    def enqueue(self, value):
        node = SNode(value, self.tail)
        if self.empty():
            self.head.nextN = node
            self.tail.nextN = node
        else:
            self.tail.nextN.nextN = node
            self.tail.nextN = node
        self.size += 1
        
    def dequeue(self):
        if not self.empty():
            value = self.head.nextN.data
            self.head.nextN = self.head.nextN.nextN
            self.size -= 1
            return value
        raise Exception("The queue is empty!")
    
    def show(self):
        print "queue size: ", self.size
        print "is empty?: ", self.empty()
        current = self.head.nextN
        count = 1
        while(count <= self.size):
            print current.data 
            current = current.nextN
            count += 1

q = Queue()
q.show()       
q.enqueue(1) 
q.enqueue(2) 
q.enqueue(3) 
q.enqueue(4) 
q.show()

q.dequeue()
q.show()
q.dequeue()
q.dequeue()
q.dequeue()
q.show()
