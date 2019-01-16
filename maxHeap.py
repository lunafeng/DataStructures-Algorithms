class MaxHeap:
    def __init__(self):
        self.H = []
        self.size = 0
        
    def insert(self, data):
        self.H.append(data)
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_max(self):
        if self.is_empty():
            print "The heap is empty"
            return
        maxVal = self.H[0]
        if self.size > 1:
            self.H[0] = self.H[self.size - 1]
            self.H = self.H[:-1]
            self.size -= 1
            self.sift_down(0)
        else:
            self.H = self.H[:-1]
            self.size -= 1
        return maxVal
            

    def sift_up(self, index):
        current = self.H[index]
        parent = self.H[index/2]
        while(index >= 1 and parent < current):
            self.H[index] = parent
            self.H[index/2] = current
            index /= 2
            current = self.H[index]
            parent = self.H[index/2]


    def sift_down(self, index):
        current = self.H[index]
        maxIndex = index
        if 2 * index + 1 < self.size:
            left = self.H[2*index + 1]
            if left > current:
                maxIndex = 2 * index + 1
        if 2 * index + 2 < self.size:
            right = self.H[2*index + 2]
            if right > left:
                maxIndex = 2 * index + 2
        if index != maxIndex:
            self.H[index] = self.H[maxIndex] 
            self.H[maxIndex] = current
            self.sift_down(maxIndex)
            

    def remove(self, index):
        if self.is_empty():
            print "The heap is empty, nothing to remove" 
        if index < self.size:
            res  = self.H[index]
            self.H[index] = float('inf')
            self.sift_up(index)
            self.extract_max()
        else:
            print "The index is out of bound"
            

    def heapify(self, arr):
        self.H = arr
        self.size = len(self.H)
        startIdx = int(0.5 * self.size)
        for idx in range(0, startIdx + 1)[::-1]:
            self.sift_down(idx)
        print self.H

    def heap_sort(self, arr):
        self.heapify(arr)
        while(self.size > 1):
            print self.H[0]
            self.H[0] = self.H[self.size - 1]
            self.H = self.H[:-1]
            self.size -= 1
            self.sift_down(0)
        print self.H[0]
        
    def get_max(self):
        return self.H[0]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def show(self):
        print self.H

test = MaxHeap()
test.insert(1)
test.insert(2)
test.insert(3)
test.insert(9)
test.insert(10)
test.insert(2)
test.insert(5)
test.insert(6)
test.insert(8)
test.insert(2)
test.show()
print test.extract_max()
test.show()
print "removing at index 3"
test.remove(3)
test.show()
test.heapify([4,2,3,7,6,5,8,10])
test.heap_sort([5,4,7,23,4,51,24,9,0])

