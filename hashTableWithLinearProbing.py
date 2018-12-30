class HashTable:
    def __init__(self, m):
        self.m = m
        self.arr = [None] * m
        self.k = []

    def add(self, key, value):
        exists = self.exists(key)
        if exists[0]:
            self.arr[exists[1]] = (key, value)
        else: 
            prehashCode = hash(key)
            index = prehashCode % self.m
            while(self.arr[index] is not None and self.arr[index] != 'Deleted'):
                index += 1
                if index >= self.m:
                    self._resize()
                    index = prehashCode % self.m
            self.arr[index] = (key, value)
            self.k.append((key,value))
        
        
    def _resize(self):
        self.m = 2 * self.m
        currentArr = self.arr
        self.arr = [None] * self.m
        self._rehash()


    def _rehash(self):
        for (key,value) in self.k:
            self.add(key, value)

    def exists(self, key):
        prehashCode = hash(key)
        index = prehashCode % self.m
        if self.arr[index] is None:
            return (False, None)
        else:
            while(self.arr[index] is not None):
                if self.arr[index][0] == key:
                    return (True,index)
                index += 1
                if index >= self.m:
                    return (False, None)
        return (False, None)
    
    def get(self, key):
        prehashCode = hash(key)
        index = prehashCode % self.m
        exists = self.exists(key)
        if exists[0]:
            return self.arr[exists[1]][1]
        else:
            raise Exception("key not found!")

    def remove(self, key):
        exists = self.exists(key)
        if exists[0]:
            self.arr[exists[1]] = "Deleted"
        else:
            raise Exception("key not found!")

    def show(self):
        print self.arr

test = HashTable(10)
test.add("luna",1)
test.show()
test.add("luna",2)
test.show()
test.add("feng",3)
test.show()
test.add("feng1",4)
test.show()
test.add("feng2",5)
test.show()
test.add("feng3",6)
test.show()
test.add("feng4",8)
test.show()
test.add("feng5",3)
test.show()
test.add("feng6",3)
test.show()
test.add("feng7",3)
test.show()
test.add("feng8",3)
test.show()
test.add("feng9",3)
test.show()
test.add("feng10",3)
test.show()
test.add("feng11",3)
test.show()
print test.get("feng11")
print test.get("luna")
test.remove("luna")
test.show()
print test.exists("feng")
